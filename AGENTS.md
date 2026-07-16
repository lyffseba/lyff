# Agent instructions — lyff hub

You are working in the **lyff offline portfolio hub** (`~/lyff`).

## Rules

1. **Offline-first.** Prefer local commands. Do not require network for status, docs, builds that can run offline.
2. **Hub vs projects.** Meta docs/scripts live at the root. Nested dirs (`43/`, `ai/`, …) are **independent git repos** — commit inside the project that owns the change, not only at hub root unless changing hub files.
3. **Registry is truth.** Project ids and offline commands are in `registry.yaml`. Update it when adding/removing projects.
4. **CLI.** Use `./bin/lyff` or `lyff` for orchestration (`status`, `doctor`, `docs`, `run`, `foreach`).
5. **Secrets.** Never commit `.env` or API keys. Use each project's `.env.example`.
6. **Branch protection.** Do not push directly to `main`/`master` on remotes that enforce PRs; use feature branches.
7. **Motto.** First do it, then do it right, then do it better.

## Quick map

| Path | What |
|------|------|
| `docs/` | Portfolio documentation |
| `bin/lyff` | Center command |
| `registry.yaml` | Project registry |
| `AGENT_STATE.md` | Hub session memory |
| `43` … `witness` | Nested product/school repos |

## Starting work

1. Read `AGENT_STATE.md` and `docs/index.md`.
2. `lyff status` then open the target project.
3. Update `AGENT_STATE.md` when finishing a hub-level task.
