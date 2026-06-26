# Installing Slide Interaction Layer

There are three ways to use this project. Pick the one that matches you — you do **not** need all
three. Start with Path 1; it's the simplest and needs no account or setup.

| Path | Best for | Needs |
| ---- | -------- | ----- |
| 1 · Local agent | Anyone with Claude Code, Codex, or Cursor | just the files |
| 2 · Claude plugin | Using it as an installable plugin in Cowork / Claude Code | the plugin manifest |
| 3 · Org marketplace | Rolling it out to a whole company | Team/Enterprise Owner |

---

## Path 1 — Local agent usage (simplest)

Use it as plain context that you point your AI coding agent at. No install, no account.

1. **Get the files.**
   ```bash
   git clone https://github.com/fidos777/slide-interaction-layer.git
   ```
   (Or download a release ZIP from the repo's Releases page and unzip it.)

2. **Tell your agent to read the skill.** In Claude Code, Codex, Cursor, or similar, say:
   ```
   Read ./slide-interaction-layer/SKILL.md as a skill.
   ```
   That loads the interaction taxonomy and the decision rules.

3. **Ask it to build a deck with `frontend-slides`.**
   ```
   Use frontend-slides to build an interactive HTML deck about <your topic>.
   Apply the taxonomy to pick the right interaction per slide. Don't overuse popups.
   ```

That's it. The agent reads `SKILL.md` + the `taxonomy/` folder and uses the `components/` as
building blocks. See [`prompts/use-with-frontend-slides.md`](prompts/use-with-frontend-slides.md)
for more ready-made prompts.

---

## Path 2 — Claude plugin usage (local / manual)

This repo is also a **Claude plugin**. The file that makes it one is
[`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) — a small manifest that gives the plugin
its name (`slide-interaction-layer`), version, and description. Any tool that understands Claude
plugins can read that manifest and install the whole folder (skill + taxonomy + components +
examples) in one step.

Two ways to use it as a plugin without an organization:

- **Claude Code (local):** add this folder (or the GitHub repo) as a plugin marketplace, then
  install the plugin from it. See Anthropic's plugin docs for the exact commands:
  <https://code.claude.com/docs/en/plugins>.
- **Manual upload (admin UI):** an organization owner can upload a plugin **ZIP** (the repo zipped,
  must be a valid `.zip` under **50 MB**) via *Organization settings → Plugins → Add plugins →
  Upload a file*. Good for quick testing before wiring up GitHub sync (Path 3).

You don't need to edit anything — `plugin.json` is already included and valid.

---

## Path 3 — Organization marketplace usage (Team / Enterprise)

For distributing the plugin to everyone in a company, through a **private** marketplace repository
that Claude syncs from.

> **Requires Team/Enterprise plan + Owner (or Primary Owner) access**, with **Cowork and Skills
> enabled** for the organization. On an individual plan, use Path 1 or Path 2 instead.

How it fits together:

1. **A separate, private marketplace repo** (e.g. `claude-plugins-marketplace`). Public repos are
   **not** allowed for organization marketplaces — it must be private or internal, on github.com.
2. That repo contains **`.claude-plugin/marketplace.json`**, which lists the plugins it offers and
   points to each one by a relative path, for example:
   ```json
   {
     "name": "fidos-plugins",
     "owner": { "name": "fidos777" },
     "plugins": [
       {
         "name": "slide-interaction-layer",
         "source": "./plugins/slide-interaction-layer",
         "description": "Interaction design system for AI-generated HTML slide decks."
       }
     ]
   }
   ```
   A copy of this plugin lives at `plugins/slide-interaction-layer/` inside that repo. (Relative
   paths are the source type that works for private marketplaces.)
3. **Connect it in Claude:** *Organization settings → Plugins → Add plugin → GitHub →
   `owner/claude-plugins-marketplace`*. An initial sync runs automatically; you can turn on
   **Sync automatically** so it updates whenever a PR is merged.
4. **Set the install preference** to **Installed by default** so every member gets it automatically
   (they can still uninstall). Other options: *Available for install*, *Not available*, *Required*.

A ready-to-run scaffold for the private marketplace repo and a step-by-step admin checklist are
provided outside this repo (the marketplace bundle and `SETUP-CHECKLIST.md`).

---

## Which should I pick?

- Just want to make slides today → **Path 1.**
- Want it as a reusable plugin on your own machine → **Path 2.**
- Want your whole team to have it automatically → **Path 3.**
