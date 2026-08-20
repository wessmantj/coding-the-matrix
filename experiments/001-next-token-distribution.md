# Experiment 001 — Next-token distribution

## The idea
Load a really small, unremarkable local model. Nothing recent, maybe something
from ~2020, and poke around. Look at how it uses tokens, and see what happens
when I change things like how much room it has to "reason."

## What it's actually testing
Instead of printing the model's sampled output, print the **top-20 next-token
probability distribution** for a given prompt. That makes the model's actual
"belief" about the next word visible, instead of one sampled word.

Target question: **capability vs. elicitation.** If a prompt change shifts the
output, did it *create* an ability or just *resurface* one already there?
Nothing is trained here, so any change is elicitation by construction — this is
a clean way to watch that happen.

**Model:** starting with a small model gpt-2: 124M.

## Prediction (write BEFORE running — getting it wrong is the point)
The real question: does a **missing apostrophe** ("Im" vs "I'm") change what the
model predicts next, and does the well-formed version predict *better*?

Why it should matter — tokenization. "I'm" splits into "I" + "'m", where "'m" is
a dedicated contraction token the model saw constantly in clean text, always in
first-person-present context. "Im" splits differently and mostly showed up in
messy, informal, low-quality text (typos, usernames). So the context signal
should be muddier.

My prediction: the typo degrades the prediction. "I'm" yields a more confident,
more grammatical next token than "Im". Open sub-question I don't know the answer
to: once more context arrives ("gonna"), does the typo's damage *persist* or does
the model wash it out and self-correct?

Test — four prompts, compare the next-token distributions:
1. "I'm"        (alone)
2. "Im"         (alone)
3. "I'm gonna"
4. "Im gonna"

Pair 1v2 = does grammar recover at the boundary. Pair 3v4 = does the damage
survive downstream.

## Setup
- `transformers` directly, we need raw logits.
- Feed one sentence; print the top-20 next-token probabilities.

## Result

> Placeholder Prompt: "The Capital of France is"
I ran this to test the file working as a whole, but the output surprised me...

' the'          0.0846
' now'          0.0479
' a'            0.0462
' France'       0.0324
' Paris'        0.0322
...

The correct answer wasn't even near the top of the distribution. Even then however, the highest
probability in the whole vocab is 8.5%. It's flat with no strong beliefs at all. So a few things I see.
First, the model is predicting grammar and the most common word after is, in English, is "the". Same with
the other tokens before "Paris". I mean, it did its job as a text continuation engine, just not what I expected.
Second, this really shows how small a 124M model is. It's dominated by local grammatical and statistical patterns
over meaning, which never occurred to me and cements why we need so much data for these models used today.

> Experiment Prompt 1: "I'm"

' not'          0.1614
' going'        0.0586
' a'            0.0503
' sure'         0.0425
' sorry'        0.0388
' just'         0.0302
' so'           0.0219
' really'       0.0176
' very'         0.0139
' still'        0.0135
' the'          0.0131
' in'           0.0131
' glad'         0.0130
' pretty'       0.0119
' trying'       0.0119
' gonna'        0.0100
' looking'      0.0100
' here'         0.0090
' also'         0.0078
' afraid'       0.0078

Gives a reasonable distribution for common English phrases, expected this here.

> Experiment Prompt 2: "Im"

'.'             0.0237
'\n'            0.0183
'-'             0.0152
','             0.0121
' the'          0.0055
':'             0.0053
'a'             0.0051
' of'           0.0050
' in'           0.0045
' and'          0.0045
' a'            0.0041
' to'           0.0038
'in'            0.0037
')'             0.0035
' ('            0.0035
'i'             0.0033
'al'            0.0032
'/'             0.0031
'_'             0.0031
' is'           0.0029

Also expected this here. The model has no idea what "Im" means and is giving punctuation majority of the distribution.

> Experiment Prompt 3: "I'm gonna"

' go'           0.0878
' be'           0.0783
' have'         0.0416
' do'           0.0372
' get'          0.0359
' take'         0.0357
' make'         0.0302
' try'          0.0269
' say'          0.0230
' give'         0.0220
' tell'         0.0212
' start'        0.0211
' keep'         0.0158
' put'          0.0145
' play'         0.0118
' leave'        0.0108
' need'         0.0104
' show'         0.0092
' run'          0.0084
' ask'          0.0081

Makes sense here as well, since it's a correct phrase it's giving a good distribution for possible tokens. Pretty flat since a lot of options.

> Experiment Prompt 4: "Im gonna"

' be'           0.0978
' go'           0.0645
' get'          0.0464
' do'           0.0354
' make'         0.0338
' take'         0.0235
' say'          0.0221
' have'         0.0209
' try'          0.0202
' play'         0.0151
' kill'         0.0135
' tell'         0.0132
' give'         0.0114
' keep'         0.0113
' leave'        0.0104
' start'        0.0096
' put'          0.0096
' just'         0.0079
' die'          0.0077
' run'          0.0076

Now this is interesting. This is nearly identical to the one above. Both correctly predict a verb, both peak around 0.09, and it's the 
same vocabulary just shuffled a little in order. So the typo damage disappeared once the token was no longer a standalone input. 


## Findings & What it changed
A missing apostrophe wrecks prediction at the token boundary ("Im" → flat punctuation) but the damage is repaired by downstream context ("Im gonna" ≈ "I'm gonna").
GPT-2's confidence tracks token co-occurrence, and strong later tokens override malformed earlier ones. So the more context it had around the grammar
mistake, the more it can predict correctly, but with fewer input tokens, the harder it is for it to make that decision versus going off the statistical best.