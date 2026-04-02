from services.ingestion_service.document_loader import DocumentLoader
from services.ingestion_service.chunker import TextChunker

from core.embeddings.local_embedder import LocalEmbedder
from core.vector_store.faiss_store import FAISSVectorStore

from services.rag_service.retriever import Retriever


def test_retriever():

    loader = DocumentLoader(
        directory="data/raw_documents"
    )

    documents = loader.load_txt_files()

    chunker = TextChunker(
        chunk_size=50,
        overlap=10
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

    query = "What does Capital One build?"

    results = retriever.retrieve(
        query
    )

    print("\nRetrieved Context:")

    for r in results:
        print(r)


if __name__ == "__main__":
    test_retriever()