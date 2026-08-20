# Landscape

The **durable** structure of AI or the parts that change slowly. Not "who's
winning this month" (that's `frontier.md`), but the shape of the field: the
recurring arguments and the axes everything moves along.


## Region 1 — Specify vs. learn

The recurring argument of the whole field: should a machine's knowledge be
**specified** by humans, or **learned** from data?

The field bet on "specify" twice and lost both times:
- **1960s** — logic and search.
- **1980s** — expert systems.

Both hit the same two walls:
1. Experts can't articulate what they know.
2. Hand-written rules don't cover the world.

Sutton's *bitter lesson* is the compressed version: general methods that scale
with computation beat hand-crafted knowledge, eventually, every time.

## Region 2 — The three scaling axes

Where progress has come from, in order:
1. **Model + data scale** (~2018–2023) — bigger model, more data.
2. **Test-time compute** (~2024–2025) — let the model think longer at
   inference.
3. **Task horizon** (2025–now) — how long a task the model completes before it
   derails.

Axis 3 is a **property of the model**, not an ops/uptime thing (I misread it
that way at first). Errors compound multiplicatively: 99% reliability per step
over 200 steps is 0.99²⁰⁰ ≈ 13% success. **Credit assignment** — knowing which
earlier step caused a late failure — is the unsolved core.
