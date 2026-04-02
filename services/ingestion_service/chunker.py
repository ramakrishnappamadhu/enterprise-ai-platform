import nltk
from typing import List

from core.logger import logger
from services.ingestion_service.document_loader import Document


class TextChunk:

    def __init__(
        self,
        content: str,
        source: str,
        chunk_id: int
    ):
        self.content = content
        self.source = source
        self.chunk_id = chunk_id


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 200
    ):
        self.chunk_size = chunk_size

    def split_documents(
        self,
        documents: List[Document]
    ) -> List[TextChunk]:

        chunks = []

        for doc in documents:

            sentences = nltk.sent_tokenize(
                doc.content
            )

            current_chunk = ""
            chunk_id = 0

            for sentence in sentences:

                if len(current_chunk) + len(sentence) <= self.chunk_size:

                    current_chunk += " " + sentence

                else:

                    chunks.append(
                        TextChunk(
                            content=current_chunk.strip(),
                            source=doc.source,
                            chunk_id=chunk_id
                        )
                    )

                    logger.info(
                        f"Created chunk {chunk_id}"
                    )

                    current_chunk = sentence
                    chunk_id += 1

            if current_chunk:

                chunks.append(
                    TextChunk(
                        content=current_chunk.strip(),
                        source=doc.source,
                        chunk_id=chunk_id
                    )
                )

        logger.info(
            f"Total chunks created: {len(chunks)}"
        )

        return chunks