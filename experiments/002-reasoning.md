# Experiment 002 — Reasoning

## The idea
Take a newer small model that actually does chain-of-thought and change how it's
allowed to reason. Two knobs, in sequence:
- **Knob A (main):** prompt it two ways on the same problems. Trying "answer directly"
  vs. "think step by step." Does eliciting reasoning make it get more right?
- **Knob B (follow-up):** vary the token budget it's allowed to spend before
  answering. Does more room help, or does it hit the same answer either way?

## What it's actually testing
Same through-line as 001: **capability vs. elicitation.** Nothing is trained, so
if step-by-step wins, the arithmetic ability was already in the weights — the
prompt just gave it room to run. This is elicitation by construction; the
question is how *strong* the effect is.

## Model
`Qwen2.5-1.5B-Instruct`. Real CoT, strong at math for its size, and
ungated. ~3 GB; generation is slower than 001's single forward pass.

---

## Knob A — direct vs. step-by-step (MAIN)

### Prediction (write BEFORE running)
Using a chain-of-thought model, telling it to "solve step by step" will make it
perform better, even if only slightly, versus answering at face value.

The *why* (sharpened): the model gets one forward pass per token. Forced to
answer immediately, it has to do all the arithmetic in that single pass. When it
writes steps out, each token it generates becomes input it can condition on for
the next. It's using its own output as a scratchpad, spreading one hard
computation across many forward passes. So it's not "understanding better," it's
getting *more compute steps*. And since nothing is trained, the ability was
always there; the direct prompt just didn't give it room. Pure elicitation.

Magnitude guess: big jump, not a small bump. I expect roughly half or more of
the direct-prompt failures to flip to correct with step-by-step. Caveat that
could shrink it: Qwen is trained to reason, so it may sneak in steps even when
told to answer directly, making "direct" less pure and the gap smaller.

### Setup
- `transformers`, `model.generate()` (not a raw forward pass).
- Wrap prompts with `tokenizer.apply_chat_template` (instruct model).
- Task: 10–20 grade-school word problems with a single numeric answer.
- Run each problem BOTH ways; extract the final number; count correct.
- Keep everything identical except the instruction line — that's the only knob.

### Result
_(after running — two counts, e.g. "direct: 6/15, step-by-step: 11/15")_

### What it changed
_(after running)_

---

## Knob B — token budget (FOLLOW-UP)

### Prediction (write BEFORE running)
_(to fill in after Knob A — likely informed by what A shows)_

### Setup
- Same model, same problems, always step-by-step.
- Vary `max_new_tokens` (e.g. 32 / 128 / 512) — how much room to reason.
- At small budgets the model gets cut off mid-reasoning; force/parse an answer
  anyway and count correct.
- Question: does accuracy climb with budget, plateau, or not move?

### Result
_(after running)_

### What it changed
_(after running)_
