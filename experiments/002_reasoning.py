import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype="auto")
model.eval()

PROBLEMS = [
    ("Sarah has 3 boxes with 12 apples each. She gives away 7 apples. How many are left?", 29),
    ("A train travels 60 miles per hour for 2.5 hours. How many miles does it go?", 150),
    ("Tom buys 4 notebooks at $3 each and pays with a $20 bill. How much change does he get?", 8),
    ("There are 24 students. Each needs 2 pencils. Pencils come in packs of 10. How many packs are needed?", 5),
    ("A rectangle is 7 cm wide and 9 cm tall. What is its area in square cm?", 63),
]

DIRECT_INSTRUCTION = "" 
STEPWISE_INSTRUCTION = ""


def ask(question, instruction, max_new_tokens):
    """Send one problem under one instruction; return the model's raw text."""
    # 1. Build the chat messages. Instruct models expect a list of role-tagged
    #    dicts, not a raw string. We put the instruction + question as the user turn.
    messages = [
        {"role": "user", "content": f"{instruction}\n\n{question}"},
    ]

    # 2. apply_chat_template formats those messages into the exact token layout
    #    Qwen was trained on (special tokens, role markers). add_generation_prompt
    #    appends the cue that it's the model's turn to speak.
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    # 3. Generate. do_sample=False = greedy (deterministic) so the experiment is
    #    reproducible. TODO: pick max_new_tokens per condition (see main loop).
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    # 4. `out` contains the PROMPT tokens + the new tokens. Slice off the prompt
    #    so we only decode what the model actually generated.
    generated = out[0][inputs.input_ids.shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True)


def extract_answer(text):
    """Pull the final number out of the model's text.
    TODO (the fiddly part): the model writes prose; you need the LAST number in
    it (the final answer usually comes last). Hint: re.findall for numbers, take
    the last match, strip commas, compare as a number. Handle 'no number found'.
    """
    numbers = re.findall(r"-?\d[\d,]*", text)  # TODO: refine if needed
    if not numbers:
        return None
    return int(numbers[-1].replace(",", ""))


def run_condition(instruction, max_new_tokens):
    """Run every problem under one instruction; return (correct, total)."""
    correct = 0
    for question, answer in PROBLEMS:
        text = ask(question, instruction, max_new_tokens)
        guess = extract_answer(text)
        # TODO: compare guess to answer, increment `correct` when they match.
        # Optionally print each so you can eyeball failures.
        pass
    return correct, len(PROBLEMS)


if __name__ == "__main__":
    # Direct gets a small budget (it should answer immediately); step-by-step
    # needs room to write its reasoning. TODO: pick sensible numbers.
    direct_correct, total = run_condition(DIRECT_INSTRUCTION, max_new_tokens=____)
    step_correct, _ = run_condition(STEPWISE_INSTRUCTION, max_new_tokens=____)

    print(f"direct:       {direct_correct}/{total}")
    print(f"step-by-step: {step_correct}/{total}")
