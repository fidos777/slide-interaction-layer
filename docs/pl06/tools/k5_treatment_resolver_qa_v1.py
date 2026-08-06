#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA for unit-specific treatment authority delegation.

The resolver owns generic F3 interpretation. Unit-specific F4 routing belongs to
pl06_authority_v1. This suite proves both the preserved B03 behaviour and the
absence of unit-specific authority literals in the shared resolver.
"""

from __future__ import annotations

import argparse
import ast
import copy
import sys
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import k5_treatment_resolver_v1 as TR
import pl06_authority_v1 as A


SUITE_ID = "K5_TREATMENT_RESOLVER_AUTHORITY_QA_v1"

B03 = "K5-PL06-T03-B03"
T05 = "K5-PL06-T05-B01"
UNKNOWN = "K5-PL06-T99-B99"

EXPECTED_RECORDS = [
    {
        "screen": "Sub-soil Drainage",
        "treatment": "Langkah demi langkah",
    },
    {
        "screen": "Swale / Natural Drain",
        "treatment": "Click-to-Reveal",
    },
]

EXPECTED_OVERRIDE_MAP = {
    "subsoildrainage": "Langkah demi langkah",
    "swalenaturaldrain": "Click-to-Reveal",
}

EXPECTED_RESULT_KEYS = {
    "unit_id",
    "screen",
    "treatment",
    "basis",
    "authority_locus",
    "reason",
    "f3_case",
    "overridden",
}

F3_CASES = (
    (
        TR.SEQUENTIAL,
        "Langkah demi langkah",
    ),
    (
        TR.COMPARISON,
        "Comparison",
    ),
    (
        TR.LAYERED,
        "Click-to-Reveal",
    ),
    (
        TR.OTHERWISE,
        "Kandungan statik",
    ),
)


class ContractFailure(RuntimeError):
    pass


def _record(
    failures: list[str],
    name: str,
    actual: Any,
    expected: Any,
) -> None:
    if actual != expected:
        failures.append(
            f"{name}: expected={expected!r} actual={actual!r}"
        )


def _call(
    failures: list[str],
    name: str,
    function: Callable[[], Any],
) -> Any:
    try:
        return function()
    except Exception as exc:
        failures.append(
            f"{name}: raised={type(exc).__name__}:{exc}"
        )
        return None


def _source_contract(
    failures: list[str],
) -> None:
    resolver_path = HERE / "k5_treatment_resolver_v1.py"
    authority_path = HERE / "pl06_authority_v1.py"

    resolver_source = resolver_path.read_text(
        encoding="utf-8"
    )
    authority_source = authority_path.read_text(
        encoding="utf-8"
    )

    forbidden_resolver_literals = (
        "b03_treatments",
        "K5-PL06-T03-B03",
        'A.value("interaction"',
        "A.value('interaction'",
    )

    leaked = [
        token
        for token in forbidden_resolver_literals
        if token in resolver_source
    ]

    _record(
        failures,
        "RESOLVER_HAS_NO_UNIT_SPECIFIC_AUTHORITY_LITERAL",
        leaked,
        [],
    )

    if "def treatment_overrides" not in authority_source:
        failures.append(
            "AUTHORITY_OWNS_TREATMENT_ROUTING:"
            " treatment_overrides function absent"
        )

    tree = ast.parse(resolver_source)

    override_nodes = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "overrides"
    ]

    _record(
        failures,
        "RESOLVER_OVERRIDES_FUNCTION_COUNT",
        len(override_nodes),
        1,
    )

    if len(override_nodes) != 1:
        return

    calls = [
        node
        for node in ast.walk(override_nodes[0])
        if isinstance(node, ast.Call)
    ]

    delegates = False

    for call in calls:
        function = call.func

        if not isinstance(function, ast.Attribute):
            continue

        if function.attr != "treatment_overrides":
            continue

        if (
            isinstance(function.value, ast.Name)
            and function.value.id == "A"
        ):
            delegates = True
            break

    _record(
        failures,
        "RESOLVER_DELEGATES_TO_AUTHORITY",
        delegates,
        True,
    )


def evaluate_contract(
    *,
    include_source: bool,
) -> list[str]:
    failures: list[str] = []

    authority_b03 = _call(
        failures,
        "AUTHORITY_B03_CALL",
        lambda: A.treatment_overrides(B03),
    )
    authority_t05 = _call(
        failures,
        "AUTHORITY_T05_CALL",
        lambda: A.treatment_overrides(T05),
    )
    authority_unknown = _call(
        failures,
        "AUTHORITY_UNKNOWN_CALL",
        lambda: A.treatment_overrides(UNKNOWN),
    )

    _record(
        failures,
        "AUTHORITY_B03_EXACT_RECORDS",
        authority_b03,
        EXPECTED_RECORDS,
    )
    _record(
        failures,
        "AUTHORITY_T05_EMPTY",
        authority_t05,
        [],
    )
    _record(
        failures,
        "AUTHORITY_UNKNOWN_EMPTY",
        authority_unknown,
        [],
    )

    fresh_first = _call(
        failures,
        "AUTHORITY_FRESH_LIST_FIRST",
        lambda: A.treatment_overrides(B03),
    )
    fresh_second = _call(
        failures,
        "AUTHORITY_FRESH_LIST_SECOND",
        lambda: A.treatment_overrides(B03),
    )

    if (
        isinstance(fresh_first, list)
        and isinstance(fresh_second, list)
    ):
        _record(
            failures,
            "AUTHORITY_RETURNS_FRESH_LIST",
            fresh_first is fresh_second,
            False,
        )

    override_b03 = _call(
        failures,
        "RESOLVER_B03_OVERRIDE_MAP_CALL",
        lambda: TR.overrides(B03),
    )
    override_t05 = _call(
        failures,
        "RESOLVER_T05_OVERRIDE_MAP_CALL",
        lambda: TR.overrides(T05),
    )
    override_unknown = _call(
        failures,
        "RESOLVER_UNKNOWN_OVERRIDE_MAP_CALL",
        lambda: TR.overrides(UNKNOWN),
    )

    _record(
        failures,
        "RESOLVER_B03_OVERRIDE_MAP",
        override_b03,
        EXPECTED_OVERRIDE_MAP,
    )
    _record(
        failures,
        "RESOLVER_T05_OVERRIDE_MAP_EMPTY",
        override_t05,
        {},
    )
    _record(
        failures,
        "RESOLVER_UNKNOWN_OVERRIDE_MAP_EMPTY",
        override_unknown,
        {},
    )

    b03_subsoil = _call(
        failures,
        "B03_SUBSOIL_RESOLVE_CALL",
        lambda: TR.resolve(
            B03,
            "Sub-soil Drainage",
            TR.OTHERWISE,
            "QA supplied F3 reason",
        ),
    )
    b03_swale = _call(
        failures,
        "B03_SWALE_RESOLVE_CALL",
        lambda: TR.resolve(
            B03,
            "Swale / Natural Drain",
            TR.SEQUENTIAL,
            "QA supplied F3 reason",
        ),
    )

    expected_b03 = (
        (
            "B03_SUBSOIL",
            b03_subsoil,
            "Langkah demi langkah",
            TR.OTHERWISE,
        ),
        (
            "B03_SWALE",
            b03_swale,
            "Click-to-Reveal",
            TR.SEQUENTIAL,
        ),
    )

    for (
        prefix,
        result,
        treatment,
        f3_case,
    ) in expected_b03:
        if not isinstance(result, dict):
            continue

        _record(
            failures,
            f"{prefix}_RESULT_SCHEMA",
            set(result),
            EXPECTED_RESULT_KEYS,
        )
        _record(
            failures,
            f"{prefix}_TREATMENT",
            result.get("treatment"),
            treatment,
        )
        _record(
            failures,
            f"{prefix}_BASIS",
            result.get("basis"),
            TR.OVERRIDE,
        )
        _record(
            failures,
            f"{prefix}_AUTHORITY_LOCUS",
            result.get("authority_locus"),
            "F4",
        )
        _record(
            failures,
            f"{prefix}_OVERRIDDEN",
            result.get("overridden"),
            True,
        )
        _record(
            failures,
            f"{prefix}_F3_CASE_PRESERVED",
            result.get("f3_case"),
            f3_case,
        )

    normalised_variants = (
        (
            "  sub soil drainage  ",
            TR.OTHERWISE,
            "Langkah demi langkah",
        ),
        (
            "SWALE---NATURAL DRAIN",
            TR.SEQUENTIAL,
            "Click-to-Reveal",
        ),
    )

    for screen, f3_case, treatment in normalised_variants:
        result = _call(
            failures,
            f"NORMALISATION_CALL:{screen}",
            lambda screen=screen, f3_case=f3_case: TR.resolve(
                B03,
                screen,
                f3_case,
                "normalisation fixture",
            ),
        )

        if not isinstance(result, dict):
            continue

        _record(
            failures,
            f"NORMALISATION_TREATMENT:{screen}",
            result.get("treatment"),
            treatment,
        )
        _record(
            failures,
            f"NORMALISATION_OVERRIDE_FLAG:{screen}",
            result.get("overridden"),
            True,
        )

    for index, (
        f3_case,
        expected_treatment,
    ) in enumerate(F3_CASES, start=1):
        reason = f"controlled F3 fixture {index}"

        result = _call(
            failures,
            f"F3_CASE_{index}_CALL",
            lambda f3_case=f3_case, reason=reason: TR.resolve(
                T05,
                f"Generic screen {index}",
                f3_case,
                reason,
            ),
        )

        if not isinstance(result, dict):
            continue

        _record(
            failures,
            f"F3_CASE_{index}_SCHEMA",
            set(result),
            EXPECTED_RESULT_KEYS,
        )
        _record(
            failures,
            f"F3_CASE_{index}_TREATMENT",
            result.get("treatment"),
            expected_treatment,
        )
        _record(
            failures,
            f"F3_CASE_{index}_BASIS",
            result.get("basis"),
            "F3_RULE_APPLIED_TO_CONTROLLED_ROWS",
        )
        _record(
            failures,
            f"F3_CASE_{index}_AUTHORITY_LOCUS",
            result.get("authority_locus"),
            "F3",
        )
        _record(
            failures,
            f"F3_CASE_{index}_OVERRIDDEN",
            result.get("overridden"),
            False,
        )
        _record(
            failures,
            f"F3_CASE_{index}_REASON",
            result.get("reason"),
            reason,
        )
        _record(
            failures,
            f"F3_CASE_{index}_CASE",
            result.get("f3_case"),
            f3_case,
        )

    if include_source:
        _source_contract(failures)

    return failures


def run_baseline() -> int:
    failures = evaluate_contract(
        include_source=True,
    )

    total = 1 if not failures else len(failures)

    print(f"SUITE_ID = {SUITE_ID}")

    if failures:
        print(
            f"0/{total} contract evaluations passed"
        )

        for failure in failures:
            print(f"  FAIL {failure}")

        return 1

    print("AUTHORITY_B03_EXACT_RECORDS=PASS")
    print("AUTHORITY_NON_B03_EMPTY=PASS")
    print("RESOLVER_AUTHORITY_DELEGATION=PASS")
    print("B03_F4_PRECEDENCE=PASS")
    print("F3_FALLBACK_MATRIX=PASS")
    print("RESOLVER_RESULT_SCHEMA=PASS")
    print("RESOLVER_NORMALISATION=PASS")
    print("RESOLVER_UNIT_NEUTRAL_SOURCE=PASS")
    print("8/8 contract groups passed")
    return 0


def run_mutations() -> int:
    original_authority = A.treatment_overrides
    original_overrides = TR.overrides
    original_resolve = TR.resolve

    def records_copy():
        return copy.deepcopy(EXPECTED_RECORDS)

    fixtures: list[
        tuple[str, Callable[[], None]]
    ] = []

    def missing_b03():
        A.treatment_overrides = (
            lambda unit_id: []
        )

    fixtures.append(
        ("M01_MISSING_B03_ROUTE", missing_b03)
    )

    def leak_t05():
        A.treatment_overrides = (
            lambda unit_id: (
                records_copy()
                if unit_id in {B03, T05}
                else []
            )
        )

    fixtures.append(
        ("M02_EXTRA_T05_ROUTE", leak_t05)
    )

    def leak_unknown():
        A.treatment_overrides = (
            lambda unit_id: (
                records_copy()
                if unit_id in {B03, UNKNOWN}
                else []
            )
        )

    fixtures.append(
        ("M03_EXTRA_UNKNOWN_ROUTE", leak_unknown)
    )

    def swapped_treatments():
        records = records_copy()
        records[0]["treatment"] = "Click-to-Reveal"
        records[1]["treatment"] = "Langkah demi langkah"

        A.treatment_overrides = (
            lambda unit_id: (
                copy.deepcopy(records)
                if unit_id == B03
                else []
            )
        )

    fixtures.append(
        ("M04_SWAPPED_B03_TREATMENTS", swapped_treatments)
    )

    def extra_record():
        records = records_copy()
        records.append({
            "screen": "Invented screen",
            "treatment": "Comparison",
        })

        A.treatment_overrides = (
            lambda unit_id: (
                copy.deepcopy(records)
                if unit_id == B03
                else []
            )
        )

    fixtures.append(
        ("M05_EXTRA_B03_RECORD", extra_record)
    )

    def resolver_ignores_authority():
        TR.overrides = lambda unit_id: {}

    fixtures.append(
        ("M06_RESOLVER_IGNORES_AUTHORITY", resolver_ignores_authority)
    )

    def missing_schema_field():
        def mutant(
            unit_id,
            screen,
            f3_case,
            reason,
        ):
            result = original_resolve(
                unit_id,
                screen,
                f3_case,
                reason,
            )
            result = dict(result)
            result.pop("authority_locus", None)
            return result

        TR.resolve = mutant

    fixtures.append(
        ("M07_RESULT_SCHEMA_FIELD_REMOVED", missing_schema_field)
    )

    def wrong_f3_otherwise():
        def mutant(
            unit_id,
            screen,
            f3_case,
            reason,
        ):
            result = original_resolve(
                unit_id,
                screen,
                f3_case,
                reason,
            )
            result = dict(result)

            if (
                unit_id != B03
                and f3_case == TR.OTHERWISE
            ):
                result["treatment"] = "Comparison"

            return result

        TR.resolve = mutant

    fixtures.append(
        ("M08_WRONG_F3_OTHERWISE_MAPPING", wrong_f3_otherwise)
    )

    def false_override_flag():
        def mutant(
            unit_id,
            screen,
            f3_case,
            reason,
        ):
            result = original_resolve(
                unit_id,
                screen,
                f3_case,
                reason,
            )
            result = dict(result)

            if unit_id == B03:
                result["overridden"] = False

            return result

        TR.resolve = mutant

    fixtures.append(
        ("M09_FALSE_F4_OVERRIDE_FLAG", false_override_flag)
    )

    escaped: list[str] = []

    for name, apply_mutation in fixtures:
        A.treatment_overrides = original_authority
        TR.overrides = original_overrides
        TR.resolve = original_resolve

        apply_mutation()

        try:
            failures = evaluate_contract(
                include_source=False,
            )
        except Exception as exc:
            failures = [
                f"caught by exception "
                f"{type(exc).__name__}:{exc}"
            ]

        caught = bool(failures)

        print(
            f"{name}="
            + ("CAUGHT" if caught else "ESCAPED")
        )

        if not caught:
            escaped.append(name)

    A.treatment_overrides = original_authority
    TR.overrides = original_overrides
    TR.resolve = original_resolve

    print(
        f"MUTATION_FIXTURES_CAUGHT="
        f"{len(fixtures) - len(escaped)}/{len(fixtures)}"
    )

    if escaped:
        print(f"ESCAPED_MUTATIONS={escaped}")
        return 1

    clean_failures = evaluate_contract(
        include_source=True,
    )

    if clean_failures:
        print(
            f"CLEAN_AFTER_MUTATIONS_FAILED="
            f"{clean_failures}"
        )
        return 1

    print("CLEAN_AFTER_MUTATIONS=PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutations",
        action="store_true",
    )
    args = parser.parse_args()

    if args.mutations:
        return run_mutations()

    return run_baseline()


if __name__ == "__main__":
    raise SystemExit(main())
