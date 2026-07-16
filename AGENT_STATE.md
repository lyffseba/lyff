# lyff — Memory Crystal (portfolio hub)

> Offline command center for documentation and orchestration of `~/lyff`.

## Current Status (2026-07-16 — do it right)

- **Hub model:** Parent git repo tracks **docs + orchestration only**. Nested projects keep independent `.git` histories (no submodules; fully usable offline once cloned).
- **Remote:** https://github.com/lyffseba/lyff (public; PR-protected `main`).
- **CLI:** `bin/lyff` v0.3 — validate, normalize int ids, bundle, foreach exit codes.
- **Tests:** `tests/test_lyff_cli.py` + `make test` + CI workflow.
- **Registry:** `registry.yaml` is the source of truth for project ids, roles, and offline commands.
- **Docs:** `docs/` + CONTRIBUTING (PR workflow).

## Projects

| id | role | offline |
|----|------|---------|
| 43 | school | full |
| 44 | product | full |
| ai | product | partial (API for chat) |
| bet | product | full |
| ents | contest | partial (demo Gemini) |
| maxi | grant | full (after pixi) |
| pi-upstream | reference | full |
| rugs | product | partial (mock agents) |
| tyypin | archive | full |
| witness | product | partial (probes) |

## Next

1. Keep registry.yaml in sync when adding/removing projects.
2. Prefer `lyff status` / `lyff doctor` before network operations.
3. `lyff bundle` for airplane tarballs; hub remote `lyffseba/lyff` when online.

---
*Agents: read this file and `docs/index.md` first when working in the lyff workspace.*
