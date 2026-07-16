# Offline-first (airplane mode)

lyff is designed so **documentation and orchestration never require the network**. Nested products may optionally call APIs when online.

## Always offline

| Capability | How |
|------------|-----|
| Portfolio map & docs | `lyff docs`, files under `docs/` |
| Project status | `lyff status`, `lyff doctor` |
| Registry | `registry.yaml` on disk |
| Libft build/test | `lyff run 43 test` |
| bet games | `lyff run bet run` |
| maxi kernel tests | after one-time local `pixi install` |
| witness / go build | `lyff run witness build` |
| tyypin build | local archive |
| ents curriculum + web demo | no key → demo Gemini responses |
| rugs UI with `AGENT_MOCK_MODE=true` | no live LLM |

## Needs network (optional)

| Capability | Why |
|------------|-----|
| Live agent chat (`ai`) | Provider APIs |
| Live ents tutor | Gemini key |
| rugs live agents | Vertex/Gemini + Supabase |
| witness probes | Provider APIs |
| `git push` / `gh` | Remotes |
| First-time `npm install` / `pixi install` / `cargo fetch` | Dependency download |

## Prep before a flight

```bash
cd ~/lyff
lyff doctor
# While online, once per machine:
lyff run ai -- npm install --ignore-scripts   # if developing ai
lyff run rugs -- npm install
lyff run maxi -- pixi install
lyff run ents -- bash -c 'python3 -m venv .venv && .venv/bin/pip install -r web/requirements.txt httpx'
lyff run bet -- cargo fetch
lyff run witness -- go mod download
```

Then disconnect. Use `lyff status` and local builds only.

## One-shot offline archive

```bash
cd ~/lyff
lyff bundle                          # → lyff-offline-YYYYMMDD-HHMMSS.tar.gz
lyff bundle /media/usb/lyff.tgz      # custom path
# later, offline machine:
tar -xzf lyff-offline-….tar.gz && cd lyff && ./bin/lyff status
```

Bundle includes nested `.git` histories and source; excludes `node_modules`, `.pixi`, `.venv`, `target`, `.env`, `*.db`.

## Hub git model

- **Hub repo** tracks docs + `bin/lyff` + registry (this offline brain).
- **Nested repos** are independent checkouts under the same directory tree — not git submodules — so nothing fetches on `git status` at the hub.
- Full offline backup: copy or tarball the entire `~/lyff` tree.
