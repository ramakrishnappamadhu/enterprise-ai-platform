from openai import OpenAI

from configs.settings import get_settings
from core.logger import logger

settings = get_settings()

client = OpenAI(
    api_key=settings.openai_api_key
)


class OpenAIEmbedder:

    def __init__(
        self,
        model: str = "text-embedding-3-small"
    ):
        self.model = model

    def generate_embedding(
        self,
        text: str
    ):

        logger.info(
            "Generating embedding"
        )

        response = client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding