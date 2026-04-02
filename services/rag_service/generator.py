from core.logger import logger


class Generator:

    def generate_answer(
        self,
        query: str,
        context_chunks
    ):

        logger.info(
            "Generating response using retrieved context"
        )

        # Remove duplicate chunks
        unique_chunks = list(set(context_chunks))

        context_text = "\n".join(
            unique_chunks
        )

        response = f"""
Query:
{query}

Answer (from retrieved context):

{context_text}
"""

        return response