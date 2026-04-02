from core.embeddings.local_embedder import LocalEmbedder


def test_local_embedding():

    embedder = LocalEmbedder()

    text = "Capital One builds scalable AI systems."

    embedding = embedder.generate_embedding(
        text
    )

    print(
        f"Embedding length: {len(embedding)}"
    )


if __name__ == "__main__":
    test_local_embedding()