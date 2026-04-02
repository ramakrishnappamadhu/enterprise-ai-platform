from pathlib import Path
from typing import List

from core.logger import logger


class Document:
    """
    Represents a loaded document.
    """

    def __init__(self, content: str, source: str):
        self.content = content
        self.source = source


class DocumentLoader:
    """
    Loads documents from disk.
    Supports TXT files initially.
    """

    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load_txt_files(self) -> List[Document]:

        documents = []

        for file_path in self.directory.glob("*.txt"):

            logger.info(f"Loading file: {file_path}")

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            documents.append(
                Document(
                    content=content,
                    source=str(file_path)
                )
            )

        logger.info(f"Loaded {len(documents)} documents")

        return documents