import faiss
import numpy as np
import os
import pickle

from core.logger import logger


class FAISSVectorStore:

    def __init__(
        self,
        dimension: int
    ):

        logger.info(
            f"Initializing FAISS index with dimension {dimension}"
        )

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.texts = []

    def add_embeddings(
        self,
        embeddings,
        texts
    ):

        logger.info(
            f"Adding {len(embeddings)} embeddings to FAISS"
        )

        embeddings_array = np.array(
            embeddings
        ).astype("float32")

        self.index.add(
            embeddings_array
        )

        self.texts.extend(texts)

    def search(
        self,
        query_embedding,
        k: int = 3
    ):

        logger.info(
            "Searching FAISS index"
        )

        query_array = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_array,
            k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.texts[idx]
            )

        return results

    # ✅ ADD THIS METHOD
    def save_index(
        self,
        path="data/vector_store"
    ):

        logger.info(
            "Saving FAISS index to disk"
        )

        os.makedirs(
            path,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            f"{path}/faiss.index"
        )

        with open(
            f"{path}/texts.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self.texts,
                f
            )

    # ✅ ADD THIS METHOD
    def load_index(
        self,
        path="data/vector_store"
    ):

        logger.info(
            "Checking for existing FAISS index"
        )

        index_file = f"{path}/faiss.index"
        texts_file = f"{path}/texts.pkl"

        if os.path.exists(index_file):

            logger.info(
                "Loading FAISS index from disk"
            )

            self.index = faiss.read_index(
                index_file
            )

            with open(
                texts_file,
                "rb"
            ) as f:

                self.texts = pickle.load(f)

            return True

        logger.info(
            "No existing index found"
        )

        return False