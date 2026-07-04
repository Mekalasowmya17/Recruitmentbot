"""
=========================================================
Embedding Model
=========================================================

Uses HuggingFace Sentence Transformers for generating
embeddings.

Author : AI Recruitment Bot
"""

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Loads the embedding model.
    """

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_embedding_model(self):
        """
        Returns embedding object.
        """
        return self.embedding


if __name__ == "__main__":

    model = EmbeddingModel()

    embedding = model.get_embedding_model()

    vector = embedding.embed_query(
        "Python Machine Learning SQL"
    )

    print("=" * 60)
    print("Embedding Length :", len(vector))
    print(vector[:10])