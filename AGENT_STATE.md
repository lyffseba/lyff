# lyff — Memory Crystal (portfolio hub)

> Offline command center for documentation and orchestration of `~/lyff`.

## Current Status (2026-08-11)

- **Hub model:** Parent git repo tracks **docs + orchestration only**. Nested projects keep independent `.git` histories (no submodules; fully usable offline once cloned).
- **Remote:** https://github.com/lyffseba/lyff (public; PR-protected `main`).
- **CLI:** `bin/lyff` v0.3 — validate, normalize int ids, bundle, foreach exit codes.
- **Tests:** `tests/test_lyff_cli.py` + `make test` + CI workflow.
- **Registry:** `registry.yaml` is the source of truth for project ids, roles, and offline commands.
- **Removed:** `ai` / `ai-coding-agent` GitHub repos deleted; local `ai/` removed from workspace.

## Projects

| id | role | offline |
|----|------|---------|
| 43 | school | full |
| 421 | school | full |
| 44 | product | full |
| bet | product | full |
| ents | contest | partial (demo Gemini) |
| maxi | grant | full (after pixi) |
| witness | product | partial (probes) |
| xai | research | full (offline notes) |

## Next

1. Keep registry.yaml in sync when adding/removing projects.
2. Prefer `lyff status` / `lyff doctor` before network operations.
3. Clean stalled local WIP in bet / mojo-music-genre-classifier / ents-cli if still needed.

---
*Agents: read this file and `docs/index.md` first when working in the lyff workspace.*
