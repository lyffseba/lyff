# Agent instructions — lyff hub

You are working in the **lyff offline portfolio hub** (`~/lyff`).

## Rules

1. **Offline-first.** Prefer local commands. Do not require network for status, docs, or builds that can run offline.
2. **Hub vs projects.** Meta docs live at the root / `docs/`. Nested dirs (`43/`, `bet/`, …) are **independent git repos** — commit inside the project that owns the change.
3. **Registry is truth.** Project ids and offline commands are in `registry.yaml`. Update it when adding/removing projects.
4. **CLI.** Use `./bin/lyff` or `lyff` for orchestration (`status`, `doctor`, `docs`, `run`, `foreach`).
5. **Secrets.** Never commit `.env` or API keys. Use each project's `.env.example`.
6. **Branch protection.** Do not push directly to `main`; use feature branches and PRs.
7. **Motto.** First do it, then do it right, then do it better.

## Quick map

| Path | What |
|------|------|
| `docs/` | Portfolio documentation |
| `bin/lyff` | Center command |
| `registry.yaml` | Project registry |
| `tests/` | Offline hub tests |
| `43, 421 … witness` | Nested product/school repos |

## Starting work

1. Read `docs/index.md` and `docs/portfolio.md`.
2. `lyff status` then open the target project.
3. Prefer updating docs over tribal knowledge in chat logs.
