# Enterprise AI Platform — Production-Ready RAG System

This project implements a **production-style Retrieval-Augmented Generation (RAG) system** using FastAPI, FAISS, and local embeddings.

It simulates real-world enterprise AI infrastructure used in industries such as **financial services, healthcare, and compliance systems**.



# 🚀 Key Features

✅ Multi-document ingestion pipeline  
✅ Sentence-based intelligent chunking  
✅ Local embedding generation  
✅ FAISS vector similarity search  
✅ Persistent vector storage (disk-based)  
✅ FastAPI REST API  
✅ Swagger UI testing interface  
✅ Multi-domain document retrieval  
✅ Modular enterprise-style architecture  



# 🧠 System Architecture
```mermaid
flowchart TD

A[User Query] --> B[FastAPI API]

B --> C[Retriever]

C --> D[Local Embedder]

D --> E[FAISS Vector Store]

E --> F[Top-K Retrieval]

F --> G[Generator]

G --> H[Response Returned to User]

subgraph Storage
I[Raw Documents]
J[Vector Store Disk Persistence]
end

I --> C
E --> J
