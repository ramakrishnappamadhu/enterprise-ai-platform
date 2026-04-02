from services.ingestion_service.document_loader import DocumentLoader
from services.ingestion_service.chunker import TextChunker


def test_chunking():

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

    print(f"Created {len(chunks)} chunks")

    for chunk in chunks:
        print(
            f"Chunk {chunk.chunk_id}: "
            f"{chunk.content[:50]}"
        )


if __name__ == "__main__":
    test_chunking()