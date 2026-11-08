from test_1.llm_config import client, MODEL


def ask(messages: list[dict]) -> str:
    response = client.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content


# --- 1. No system prompt, plain question ---
print("=== Plain ===")
print(ask([{"role": "user", "content": "Classify the sentiment: 'The delivery was late but the product is great.'"}]))

# --- 2. With a system prompt constraining output format ---
print("\n=== With system prompt ===")
print(ask([
    {"role": "system", "content": "You are a sentiment classifier. Respond with exactly one word: POSITIVE, NEGATIVE, or MIXED. No explanation."},
    {"role": "user", "content": "Classify the sentiment: 'The delivery was late but the product is great.'"}
]))

# --- 3. Few-shot: examples instead of instructions ---
print("\n=== Few-shot ===")
print(ask([
    {"role": "system", "content": "Classify sentiment. Respond with exactly one word."},
    {"role": "user", "content": "'Amazing service, highly recommend.'"},
    {"role": "assistant", "content": "POSITIVE"},
    {"role": "user", "content": "'Terrible experience, never again.'"},
    {"role": "assistant", "content": "NEGATIVE"},
    {"role": "user", "content": "'The delivery was late but the product is great.'"}
]))