# lyff

**Offline portfolio hub** — documentation and orchestration center for everything under this directory.

**Remote:** [github.com/lyffseba/lyff](https://github.com/lyffseba/lyff) (public hub meta-repo; nested products keep their own remotes)

```text
~/lyff          ← you are here (hub)
  docs/         ← portfolio docs
  bin/lyff      ← center command
  registry.yaml ← project source of truth
  43/ ai/ bet/ …← nested independent repos
```

> First do it, then do it right, then do it better.

## Fully offline by design

- Hub commands never call the network.
- Nested projects are **not** git submodules (no surprise fetches).
- Docs and status work on a plane; see [docs/offline.md](docs/offline.md).

## Install the center command

```bash
cd ~/lyff
make install
# ensures ~/.local/bin is on PATH, then:
lyff status
lyff doctor
lyff docs
```

Without install:

```bash
./bin/lyff status
```

## Common commands

| Command | What it does |
|---------|----------------|
| `lyff status` / `summary` | Status table or one-screen dashboard |
| `lyff doctor` / `prep` | Healthcheck / offline dep checklist |
| `lyff list` | Registry summary (`--json` for agents) |
| `lyff docs offline` | Airplane-mode guide |
| `lyff run bet build` | Registry command in a project |
| `lyff bundle` | Airplane tarball (+ `MANIFEST.json`) |
| `lyff completion bash` | Shell completion (also `share/lyff.sh`) |

## Documentation

Start at **[docs/index.md](docs/index.md)**.

| Doc | |
|-----|--|
| [docs/portfolio.md](docs/portfolio.md) | Project map |
| [docs/orchestration.md](docs/orchestration.md) | CLI details |
| [docs/philosophy.md](docs/philosophy.md) | Why this shape |
| [AGENTS.md](AGENTS.md) | Instructions for coding agents |
| [AGENT_STATE.md](AGENT_STATE.md) | Hub session memory |

## Nested projects

| Dir | Purpose |
|-----|---------|
| `43` | 42 school (Libft) |
| `44` | 3D Piscine World |
| `ai` | Engineer agent CLI |
| `bet` | Terminal games |
| `ents` | Ents Academy |
| `maxi` | Mojo/MAX kernels |
| `pi-upstream` | pi reference |
| `rugs` | Iberian Rugs store |
| `tyypin` | Superseded agent (local archive) |
| `witness` | Model probes |
| `sable` | Private pre-MVP |

Each has its own `.git` and (usually) its own GitHub remote. The hub only tracks **docs + orchestration**.

## Quality

```bash
make test           # offline unit tests
./bin/lyff validate
./bin/lyff doctor
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the PR workflow (`main` is protected).

## Hub git

```bash
cd ~/lyff
git status          # hub meta only
# product code changes: cd into project, commit there
```

License: [MIT](LICENSE).
