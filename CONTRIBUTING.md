# Contributing to the lyff hub

This repository is the **offline portfolio hub** (docs + orchestration only). Nested product code lives in sibling directories with their own git remotes.

## Branch protection

`main` requires a pull request (no direct pushes, no force-push).

```bash
cd ~/lyff
git switch -c feat/my-change
# edit hub files only (docs/, bin/, registry.yaml, …)
git add -A && git commit -m "…"
git push -u origin HEAD
gh pr create --fill
gh pr merge --merge --delete-branch
git switch main && git pull
```

Emergency local override only: `ALLOW_PROTECTED_PUSH=1 git push` (discouraged).

## What belongs here

| Include | Do not include |
|---------|----------------|
| `docs/`, `bin/lyff`, `registry.yaml` | Nested project source (already gitignored) |
| Hub tests, CI, Makefile | Secrets, `.env`, API keys |
| AGENT_STATE / AGENTS updates | Large binaries, node_modules |

Product changes: `cd` into the project and commit there.

## Local checks (offline)

```bash
make test          # unit tests
./bin/lyff validate
./bin/lyff doctor
./bin/lyff status
```

## Registry

When adding a project under `~/lyff/<id>/`:

1. Ensure it has its own `.git`.
2. Add an entry to `registry.yaml` (quote numeric ids like `"43"`).
3. Run `lyff validate` and `lyff status`.
