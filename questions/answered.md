# Answered

Questions I've actually answered — my real progress metric. This file is mine.
(Claude scaffolded this template once, on my explicit approval; the answers are
mine to write.)

## Template — copy this per answer
<!--
## <question, in one line>
- **Answered:** <YYYY-MM-DD>
- **Short version:** <the answer in a sentence or two>
- **How I know:** <what convinced me — read it / ran it / reasoned it through>
- **What it opened:** <new question, or [[link]], if any>
-->

---

## What are they finding now? (the current bet vs. earlier ones)
- **Answered:** 2026-08
- **Short version:**
  > So far the question I got answered that stuck with me was what they are
  > finding now. In 2020 it was more data/larger model makes it smarter,
  > extending the time it has to reason in 2022-2023, and now how long it can
  > go without human intervention and not halucinate, thats the short version.
- **How I know:**
  > I was given the history for when models really accelled past checkers and chess games; the
  > countless winters of Artificial Intelligence are no more since we have them so capable. 
- **What it opened:**

## What do models actually do when they "predict next token"?
- **Answered:** 2026-08
- **Short version:**
  > For GPT-2, its only supposed to, given some text, guess the next token. The
  > token isn't even a word, its usually a word-piece. Also, its not outputting a
  > single guess, its scoring every token in its vocabulary and outputting the  
  > spread. The scores for each vocab word is a logits, which when run through softmax,
  > turns them into a probability where they all add up to the probability distribution, or 1.0.
- **How I know:**
  > I am seeing that it splits words, so for "don't" it splits it into two tokens "don" and "'t". Also,
  > Claude confirmed my idea.
- **What it opened:**

## Where does gradient compute come in?
- **Answered:** 2026-08
- **Short version:**
  > During training, you know the correct token output for a given input. The model outputs
  > its ditribution and the loss function is used to measure how wrong it is. So, you essentially check
  > what distribution the model assigned to the correct token, and if it was near 1.0, small loss; lower means
  > more loss. 
- **How I know:**
  > In `001-next-token-distribution` I was wondering what torch.no_grad() meant. It turns the
  > token prediction I'm looking at is what they see in training and will change weights based on what
  > the models loss is on given predictions. With LLM's, this is probably done billions of times faster than 
  > by hand, but still good to know.
  > ALSO, to add onto the no_grad(), it is there since I'm not training. I don't need to record to backprop later and 
  > change weights. So I tell it don't bother and I only want the answer. This skills, loss backprop to gradient and then nudging the weights.
- **What it opened:**