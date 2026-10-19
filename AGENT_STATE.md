# lyff — Memory Crystal (portfolio hub)

> Offline command center for documentation and orchestration of `~/lyff`.

## Stack docs (2026-10-19)

- `docs/stack.md` pins tools this tip invokes to latest stable official docs (reviewed 2026-10-19).
- Node.js Active LTS pin is 24.22.0 (npm 11.19.1) through 2026-10-28; the rule then points at 26.x. Rust stable is 1.99.1 (blog 2026-10-15). pixi is 0.82.0. Python stable pin stays 3.15.0 (3.16.0a1 is a prerelease).
- Drift, repo vs those pins: CI Python `3.12` vs 3.15.0; `actions/checkout@v4` vs v7.0.1; `actions/setup-python@v5` vs v7.0.0; PyYAML and pip unpinned; `ubuntu-latest` is still Ubuntu 24.04 in the runner-images README while the 2026-10-19–11-19 move to 26.04 is open. Git, Make, Bash, zsh, Node, npm, Cargo, Go, pixi, and `cc` are presence checks with no version pin.

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
