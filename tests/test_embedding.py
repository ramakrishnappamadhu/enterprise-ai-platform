from core.embeddings.openai_embedder import OpenAIEmbedder


def test_embedding():

    embedder = OpenAIEmbedder()

    text = "Capital One builds AI systems."

    embedding = embedder.generate_embedding(
        text
    )

    print(
        f"Embedding length: {len(embedding)}"
    )


if __name__ == "__main__":
    test_embedding()