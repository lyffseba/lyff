# lyff documentation

**lyff** is the offline command center for the portfolio directory at `~/lyff`.

> First do it, then do it right, then do it better.

## Start here

| Doc | Purpose |
|-----|---------|
| [offline.md](offline.md) | Airplane-mode rules and what works without network |
| [portfolio.md](portfolio.md) | Map of every nested project |
| [orchestration.md](orchestration.md) | `lyff` CLI and Makefile |
| [philosophy.md](philosophy.md) | How the hub thinks about tools and agents |

## Center command

```bash
# from anywhere after install
lyff status
lyff doctor
lyff docs
lyff run bet build
lyff foreach status

# or from repo root
./bin/lyff status
make help
```

## Hub layout

```text
lyff/
├── bin/lyff           # center CLI
├── docs/              # this documentation
├── registry.yaml      # project registry (source of truth)
├── AGENTS.md          # instructions for coding agents
├── AGENT_STATE.md     # hub session memory
├── Makefile
├── README.md
└── <projects>/        # independent nested git repos (local checkouts)
```

## Nested projects (summary)

| id | Role | Offline |
|----|------|---------|
| **43** | 42 curriculum (Libft) | full |
| **44** | 3D Piscine campus | full |
| **ai** | Engineer agent CLI | build offline; chat needs API |
| **bet** | Terminal games | full |
| **ents** | Ents Academy / XPRIZE | curriculum + demo web offline |
| **maxi** | Mojo/MAX kernels | full after `pixi install` |
| **pi-upstream** | pi reference mirror | full |
| **rugs** | Iberian Rugs store | mock agents offline |
| **tyypin** | Superseded Rust agent | archive |
| **witness** | Model fingerprinting | build offline; probes need keys |

Deep links: open each project's own `README.md` after `lyff open <id>`.
