# Experiment 001 — Next-token distribution

## The idea (my words)
Load a really small, unremarkable local model — nothing recent, maybe something
from ~2022 — and poke around. Look at how it uses tokens, and see what happens
when I change things like how much room it has to "reason."

## What it's actually testing
Instead of printing the model's sampled output, print the **top-20 next-token
probability distribution** for a given prompt. That makes the model's actual
"belief" about the next word visible, instead of one sampled word.

Target question: **capability vs. elicitation.** If a prompt change shifts the
output, did it *create* an ability or just *resurface* one already there?
Nothing is trained here, so any change is elicitation by construction — this is
a clean way to watch that happen.

## Decision
Do the two axes in sequence:
- **001 (this file)** — next-token distribution on an old model. No reasoning
  knob; that would be meaningless on a 2022 model.
- **002** — reasoning length, on a newer small model. See
  `experiments/002-reasoning-length.md`.

**Model:** start with GPT-2 small (124M) — the canonical poke-around model,
loads instantly, raw logits are trivial to read. If you want an actual 2022
model, OPT-1.3B (Meta, 2022) is the clean swap. Both fit easily on the M3 Pro
/ 18 GB (MPS backend).

## Prediction (write BEFORE running — getting it wrong is the point)
_(to fill in)_

## Setup
- `transformers` directly, not Ollama — we need raw logits.
- Feed one sentence; print the top-20 next-token probabilities.

## Result
_(after running)_

## What it changed
_(what I believe now that I didn't before)_
