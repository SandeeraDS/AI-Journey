import numpy as np
from test_1.llm_config import client


def embed(text: str) -> list[float]:
    response = client.embeddings.create(model="nomic-embed-text", input=text)
    return response.data[0].embedding


def cosine_similarity(a: list[float], b: list[float]) -> float:
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


sentences = [
    "The cat sat on the mat.",
    "A feline rested on the rug.",
    "The stock market crashed yesterday.",
    "Equity prices fell sharply in trading.",
    "I love eating pizza on weekends.",
]

vectors = [embed(s) for s in sentences]

print(f"Embedding dimension: {len(vectors[0])}")
print()

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        sim = cosine_similarity(vectors[i], vectors[j])
        print(f"{sim:.3f}  |  '{sentences[i]}'  <->  '{sentences[j]}'")