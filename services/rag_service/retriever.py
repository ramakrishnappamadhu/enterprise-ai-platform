from core.logger import logger


class Retriever:

    def __init__(
        self,
        vector_store,
        embedder
    ):

        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve(
        self,
        query: str,
        k: int = 3
    ):

        logger.info(
            f"Retrieving context for query: {query}"
        )

        query_embedding = self.embedder.generate_embedding(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            k
        )

        return results