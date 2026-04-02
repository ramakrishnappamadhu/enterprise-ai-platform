from services.ingestion_service.document_loader import DocumentLoader


def test_loader():

    loader = DocumentLoader(
        directory="data/raw_documents"
    )

    docs = loader.load_txt_files()

    print(f"Loaded {len(docs)} documents")

    for doc in docs:
        print(doc.source)
        print(doc.content[:100])


if __name__ == "__main__":
    test_loader()