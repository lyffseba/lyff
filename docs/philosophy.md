# Philosophy

## One directory, many minds

**lyff** is not a monorepo that flattens every product into one history. It is a **workspace**: one place to stand, document, and orchestrate, while each project remains a sovereign codebase.

## Offline is a feature

If the network dies, the map, docs, and local builds should still work. Live LLM calls are optional accelerators, not load-bearing walls. Demo modes and mock agents exist for that reason.

## First do it → right → better

Ship thin slices, then harden, then deepen. The hub itself follows that: registry + CLI first, richer docs and automation next.

## Agents read the crystal

`AGENT_STATE.md` and per-project memory files are the handoff layer between human sessions and coding agents. Prefer updating them over tribal knowledge in chat logs.
