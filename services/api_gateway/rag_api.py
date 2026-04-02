from fastapi import FastAPI
from pydantic import BaseModel

from services.ingestion_service.document_loader import DocumentLoader
from services.ingestion_service.chunker import TextChunker

from core.embeddings.local_embedder import LocalEmbedder
from core.vector_store.faiss_store import FAISSVectorStore

from services.rag_service.retriever import Retriever
from services.rag_service.generator import Generator

from core.logger import logger


# Request schema
class QueryRequest(BaseModel):
    query: str


# Create FastAPI app
app = FastAPI(
    title="Enterprise RAG API",
    version="1.0"
)


# Build RAG system on startup
@app.on_event("startup")
def startup_event():

    global retriever
    global generator

    logger.info("Starting RAG system...")

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

    # Create vector store
    vector_store = FAISSVectorStore(
        dimension=len(embeddings[0])
    )

    # Try loading existing index
    loaded = vector_store.load_index()

    if not loaded:

        logger.info("Building new FAISS index")

        vector_store.add_embeddings(
            embeddings,
            texts
        )

        vector_store.save_index()

    retriever = Retriever(
        vector_store,
        embedder
    )

    generator = Generator()

    logger.info("RAG system ready.")


# Health check route
@app.get("/")
def root():

    return {
        "status": "ok",
        "message": "RAG API running"
    }


# Main RAG route
@app.post("/ask")
def ask_question(
    request: QueryRequest
):

    query = request.query

    logger.info(
        f"Received query: {query}"
    )

    retrieved_context = retriever.retrieve(
        query
    )

    response = generator.generate_answer(
        query,
        retrieved_context
    )

    return {
        "query": query,
        "answer": response
    }