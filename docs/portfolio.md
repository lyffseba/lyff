# Portfolio map

All paths relative to `~/lyff`.

## Active products

### ai — engineer-first agent CLI
- **Path:** `ai/`
- **Remote:** github.com/lyffseba/ai-coding-agent
- **Stack:** TypeScript monorepo (pi fork)
- **Notes:** Canonical agent. Spawns **bet** for `/play`. See also **witness** philosophy.

### bet — terminal game hub
- **Path:** `bet/`
- **Remote:** github.com/lyffseba/bet
- **Stack:** Rust + Ratatui
- **Offline:** fully

### rugs — Iberian Rugs hybrid store
- **Path:** `rugs/`
- **Remote:** github.com/lyffseba/rugs (private)
- **Stack:** Next.js, Supabase, Gemma agents
- **Offline:** mock agents + local UI

### witness — model transparency probes
- **Path:** `witness/`
- **Remote:** github.com/lyffseba/witness (private)
- **Stack:** Go
- **Offline:** build/test; live probes need keys

### 44 — Piscine World
- **Path:** `44/`
- **Remote:** github.com/lyffseba/44
- **Stack:** Three.js + Express
- **Offline:** fully after npm install

## School & grants

### 43 — École 42 store
- **Path:** `43/` — Libft (+ Subject PDFs)
- **Remote:** github.com/lyffseba/43

### ents — Ents Academy
- **Path:** `ents/`
- **Remote:** github.com/lyffseba/ents
- **Role:** XPRIZE education + curriculum (JAX/MLX/MAX/Mojo)

### maxi — Modular MAX kernels
- **Path:** `maxi/`
- **Remote:** github.com/lyffseba/maxi (private)
- **Role:** Community grant kernel work

## Reference & archive

### pi-upstream
- **Path:** `pi-upstream/`
- **Remote:** github.com/earendil-works/pi
- **Role:** Read-only base for the **ai** fork — do not product-develop here

### tyypin
- **Path:** `tyypin/`
- **Remote:** deleted (superseded)
- **Role:** Local archive; canonical is **ai**

## Lineage

```text
pi-upstream (reference)
    └── ai (canonical agent)  ← tyypin (archive)
            └── /play → bet

ents (education / contest)
maxi (kernels / grant)
rugs (commerce / hybrid agents)
witness (transparency / philosophy)
43, 44 (42 school)
```
