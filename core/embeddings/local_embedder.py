from sentence_transformers import SentenceTransformer

from core.logger import logger


class LocalEmbedder:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):

        logger.info(
            f"Loading embedding model: {model_name}"
        )

        self.model = SentenceTransformer(
            model_name
        )

    def generate_embedding(
        self,
        text: str
    ):

        logger.info(
            "Generating local embedding"
        )

        embedding = self.model.encode(
            text
        )

        return embedding