from services.ingestion_service.document_loader import DocumentLoader
from services.ingestion_service.chunker import TextChunker

from core.embeddings.local_embedder import LocalEmbedder
from core.vector_store.faiss_store import FAISSVectorStore

from services.rag_service.retriever import Retriever
from services.rag_service.generator import Generator


def test_rag():

    loader = DocumentLoader(
        directory="data/raw_documents"
    )

    documents = loader.load_txt_files()

    chunker = TextChunker(
    chunk_size=200
  )

    chunks = chunker.split_documents(
        documents
    )

    embedder = LocalEmbedder()

    embeddings = []
    texts = []

    for chunk in chunks:

        emb = embedder.generate_embedding(
            chunk.content
        )

        embeddings.append(emb)
        texts.append(chunk.content)

    vector_store = FAISSVectorStore(
        dimension=len(embeddings[0])
    )

    vector_store.add_embeddings(
        embeddings,
        texts
    )

    retriever = Retriever(
        vector_store,
        embedder
    )

    generator = Generator()

    query = "What does Capital One build?"

    retrieved_context = retriever.retrieve(
        query
    )

    response = generator.generate_answer(
        query,
        retrieved_context
    )

    print("\nFinal RAG Response:\n")

    print(response)


if __name__ == "__main__":
    test_rag()