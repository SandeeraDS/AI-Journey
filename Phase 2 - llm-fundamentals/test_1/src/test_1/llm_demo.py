from test_1.llm_config import client, MODEL

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "What is 2+2? Answer in one short sentence."}
    ],
)

print(response.choices[0].message.content)
print("---")
print("Response :",response)
print("Model used:", response.model)
print("Tokens:", response.usage)