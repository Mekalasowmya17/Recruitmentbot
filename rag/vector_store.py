"""
=========================================================
Vector Store
=========================================================

Stores resume embeddings in ChromaDB.

Author : AI Recruitment Bot
"""

import os
from langchain_chroma import Chroma
from langchain_core.documents import Document

from rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.persist_directory = "chroma_db"

        self.embedding_model = EmbeddingModel().get_embedding_model()

    def build_documents(self, resumes):

        documents = []

        for resume in resumes:

            doc = Document(

                page_content=resume["content"],

                metadata={

                    "id": resume["id"],

                    "category": resume["category"]

                }

            )

            documents.append(doc)

        return documents

    def create_db(self, resumes):

        docs = self.build_documents(resumes)

        db = Chroma.from_documents(

            documents=docs,

            embedding=self.embedding_model,

            persist_directory=self.persist_directory

        )

        print("=" * 60)
        print("Vector Database Created Successfully")
        print(f"Total Documents : {len(docs)}")
        print("=" * 60)

        return db

    def load_db(self):

        if not os.path.exists(self.persist_directory):

            raise FileNotFoundError(
                "Vector Database not found.\nRun ingest.py first."
            )

        db = Chroma(

            persist_directory=self.persist_directory,

            embedding_function=self.embedding_model

        )

        return db