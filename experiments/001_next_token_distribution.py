from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

inputs = tokenizer("Im gonna", return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)          
logits = outputs.logits

next_token_logits = logits[0, -1] 

probs = torch.softmax(next_token_logits, dim=-1)

topk = torch.topk(probs, 20)  

for prob, token_id in zip(topk.values, topk.indices):
    token = tokenizer.decode([token_id])
    print(f"{token!r:15} {prob.item():.4f}")