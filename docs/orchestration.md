# Orchestration

## `lyff` CLI

Installed from `bin/lyff` to `~/.local/bin/lyff` via `make install`.

| Command | Description |
|---------|-------------|
| `lyff` / `lyff help` | Help |
| `lyff status` | All projects: branch, dirty, head, offline flag |
| `lyff doctor` | Toolchain + missing dirs + dirty nested repos |
| `lyff list` | Registry table |
| `lyff docs [topic]` | Open/print docs (`index`, `offline`, `portfolio`, …) |
| `lyff info <id>` | One project from registry |
| `lyff run <id> <cmd>` | Run a named command from registry (`build`, `test`, …) |
| `lyff run <id> -- <shell…>` | Arbitrary command in project dir |
| `lyff foreach <git-or-shell…>` | Run in every project (`status`, `fetch` not default) |
| `lyff open <id>` | `cd` helper (prints path; use `cd $(lyff path <id>)`) |
| `lyff path <id>` | Print absolute path |
| `lyff bundle [out.tgz]` | Airplane tarball (excludes `node_modules`, `.pixi`, `.venv`, secrets) |
| `lyff validate` | Validate registry paths and ids |
| `lyff version` | CLI version |
| `lyff registry` | Print `registry.yaml` path |

## Quality checks

```bash
make test       # unittest (offline)
make validate
make test-cli
```

Hub CI (GitHub Actions) runs the same offline tests on PRs to `main`.

## Makefile

```bash
make help
make status
make doctor
make install    # symlink bin/lyff → ~/.local/bin/lyff
make docs
```

## Design principles

1. **No network by default** — no auto `git fetch`, no API calls in hub commands.
2. **Registry-driven** — add a project by editing `registry.yaml`, not hardcoding the CLI.
3. **Nested independence** — each product keeps its own git history and remotes.
4. **Agent-friendly** — `AGENTS.md` + `AGENT_STATE.md` for coding agents landing in the hub.

## v0.3 extras

| Command | |
|---------|--|
| `lyff summary [--json]` | Dashboard: dirty/missing/offline counts |
| `lyff status --json` | Machine-readable status for agents |
| `lyff discover` | Git dirs under hub not in registry |
| `lyff prep` | Offline dependency checklist |
| `lyff completion bash\|zsh` | Shell completion script |
| `lyff bundle` | Includes `MANIFEST.json` with project heads |

Shell:

```bash
source ~/lyff/share/lyff.sh   # lyffcd <id> + completions
# or
eval "$(lyff completion bash)"
```
