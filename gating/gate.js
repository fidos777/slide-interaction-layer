/*!
 * Slide Interaction Layer — Completion Gating Runtime (gate.js) — v0.2.0
 * OPTIONAL + OPT-IN. Does nothing unless a stage element sets data-sil-gating="on" | "training".
 * Engine-agnostic, fail-open (any error => deck stays fully navigable), accessibility-aware.
 *
 * It blocks ONLY forward navigation on slides whose REQUIRED gated interactions are not yet
 * complete. Backward navigation is always allowed. It reads the signals components already emit
 * (data-complete / data-completion); no component changes are required.
 *
 * Public API (for engines/tests): window.SILGate.canLeave(index) -> bool,
 *   .isSatisfied(index) -> bool, .refresh(), .mode, ._state
 */
(function () {
  'use strict';

  function init() {
    try {
      var stage = document.querySelector('[data-sil-gating]');
      if (!stage) return;                                  // not opted in
      var mode = (stage.getAttribute('data-sil-gating') || 'off').toLowerCase();
      if (mode !== 'on' && mode !== 'training') return;    // off => inert

      var GATEABLE = ['reveal-cards', 'hotspot', 'quiz', 'branching', 'calculator',
                      'timeline', 'before-after', 'drag-match'];  // +P9/P10/P11 (v0.6.0)
      var slideSel = stage.getAttribute('data-sil-slide-selector') || '.slide';
      var slides = [].slice.call(stage.querySelectorAll(slideSel));
      var userChanged = new WeakMap();   // calculator strict "user_changed"
      var attempted = new WeakMap();      // quiz "attempted" (non-training opt-in)

      function isGateable(c) { return GATEABLE.indexOf(c.getAttribute('data-sil')) >= 0; }

      function gateableIn(slide) {
        return [].slice.call(slide.querySelectorAll('[data-sil]')).filter(isGateable);
      }

      function ruleFor(c) {
        var ov = c.getAttribute('data-gate'); if (ov) return ov;          // explicit override wins
        var p = c.getAttribute('data-sil');
        if (p === 'calculator') return 'user_changed';                    // strict by decision
        if (p === 'quiz') return 'answered_correctly';                    // training default
        return c.getAttribute('data-completion') || 'complete';
      }

      function satisfiedC(c) {
        var rule = ruleFor(c);
        if (rule === 'user_changed') return userChanged.get(c) === true;
        if (rule === 'attempted') return attempted.get(c) === true || c.getAttribute('data-complete') === 'true';
        // answered_correctly / all_*_ / reached_an_ending / complete => trust the component flag
        return c.getAttribute('data-complete') === 'true';
      }

      function requiredIn(slide) {
        return gateableIn(slide).filter(function (c) {
          var req = c.getAttribute('data-required');
          if (req === 'true') return true;
          if (req === 'false') return false;
          if (mode === 'training') return true;                            // training: all gateable required
          return slide.getAttribute('data-sil-gate') === 'required';       // on: only flagged slides
        });
      }

      function isSatisfied(slide) {
        if (!slide) return true;
        return requiredIn(slide).every(satisfiedC);
      }

      function progress(slide) {
        var req = requiredIn(slide), done = req.filter(satisfiedC).length;
        return { done: done, total: req.length };
      }

      function currentIndex() {
        for (var i = 0; i < slides.length; i++) {
          if (slides[i].classList.contains('active')) return i;
        }
        return 0;
      }

      function canLeave(i) { return isSatisfied(slides[i]); }

      // --- attach listeners for strict calculator + opt-in attempted-quiz ---
      slides.forEach(function (slide) {
        gateableIn(slide).forEach(function (c) {
          if (c.getAttribute('data-sil') === 'calculator') {
            var mark = function () { userChanged.set(c, true); update(); };
            c.addEventListener('input', mark, true);
            c.addEventListener('change', mark, true);
            c.addEventListener('click', function (e) {
              if (e.target && e.target.closest && e.target.closest('button,input')) mark();
            }, true);
          }
          if (ruleFor(c) === 'attempted') {
            c.addEventListener('click', function () { attempted.set(c, true); update(); }, true);
          }
        });
      });

      // --- accessible hint (non-modal, polite) ---
      var hint = document.createElement('div');
      hint.className = 'sil-gate-hint';
      hint.setAttribute('role', 'status');
      hint.setAttribute('aria-live', 'polite');
      hint.style.cssText = 'position:fixed;left:50%;bottom:64px;transform:translateX(-50%);' +
        'background:#111;color:#fff;border:1px solid rgba(255,255,255,.25);border-radius:10px;' +
        'padding:10px 16px;font:14px system-ui,sans-serif;z-index:99999;display:none;max-width:80vw;text-align:center';
      (document.body || document.documentElement).appendChild(hint);
      function showHint(msg) { hint.textContent = msg; hint.style.display = 'block'; }
      function hideHint() { hint.style.display = 'none'; }

      function navControls() {
        var sel = stage.getAttribute('data-sil-next-selector') || '[data-sil-next]';
        return [].slice.call(document.querySelectorAll(sel));
      }

      function update() {
        var i = currentIndex(), slide = slides[i], sat = isSatisfied(slide);
        navControls().forEach(function (n) { n.setAttribute('aria-disabled', sat ? 'false' : 'true'); });
        if (sat) hideHint();
        SIL._state = { index: i, satisfied: sat, progress: progress(slide) };
        return sat;
      }

      function blockFeedback() {
        var slide = slides[currentIndex()], pr = progress(slide);
        showHint('Complete this activity to continue — ' + pr.done + ' of ' + pr.total + ' done');
        var inc = requiredIn(slide).filter(function (c) { return !satisfiedC(c); })[0];
        if (inc) {
          var f = inc.querySelector('button, input, a, [tabindex]');
          if (f && f.focus) { try { f.focus(); } catch (e) {} }
        }
      }

      function isForwardKey(e) {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') return true;
        if (e.key === ' ' || e.key === 'Spacebar') {
          var a = document.activeElement;
          if (a && a.closest && a.closest('[data-sil]')) return false;   // let component use Space
          return true;
        }
        return false;
      }

      // capture-phase: runs before the engine's bubble-phase handlers
      window.addEventListener('keydown', function (e) {
        if (!isForwardKey(e)) return;
        if (!canLeave(currentIndex())) { e.preventDefault(); e.stopImmediatePropagation(); blockFeedback(); }
      }, true);

      document.addEventListener('click', function (e) {
        var i = currentIndex();
        if (e.target.closest('[data-sil-next]')) {
          if (!canLeave(i)) { e.preventDefault(); e.stopImmediatePropagation(); blockFeedback(); }
          return;
        }
        var dot = e.target.closest('button');
        if (dot && dot.parentElement && dot.parentElement.matches &&
            (dot.parentElement.matches('#dots') || dot.parentElement.matches('.dots'))) {
          var dots = [].slice.call(dot.parentElement.children);
          var target = dots.indexOf(dot);
          if (target > i && !canLeave(i)) { e.preventDefault(); e.stopImmediatePropagation(); blockFeedback(); }
        }
      }, true);

      // live re-evaluation: completion flags + active-slide changes
      var mo = new MutationObserver(function () { update(); });
      mo.observe(stage, { subtree: true, attributes: true, attributeFilter: ['data-complete', 'class'] });
      document.addEventListener('sil:complete', function () { update(); }, true);

      var SIL = window.SILGate = window.SILGate || {};
      SIL.canLeave = canLeave;
      SIL.isSatisfied = function (idx) { return isSatisfied(slides[idx]); };
      SIL.refresh = update;
      SIL.mode = mode;
      SIL._state = {};
      update();
    } catch (err) {
      // FAIL-OPEN: never break navigation because of the gate.
      if (window.console && console.warn) console.warn('SILGate disabled (fail-open):', err);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
