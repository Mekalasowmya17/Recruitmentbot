"""
=========================================================
Ingest Pipeline
=========================================================

Loads Resume.csv, splits resumes into chunks,
and stores them in ChromaDB.

Author : AI Recruitment Bot
"""

import os
import pandas as pd

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vector_store import VectorStore


class ResumeIngestion:

    def __init__(self):

        self.csv_path = "data/resumes/Resume.csv"

        self.text_splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,

            chunk_overlap=100

        )

    def load_dataset(self):

        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"{self.csv_path} not found.")

        df = pd.read_csv(self.csv_path)

        # Use only first 100 resumes during development
        df = df.head(100)

        print(f"\nLoaded {len(df)} resumes.\n")

        return df

    def create_documents(self):

        df = self.load_dataset()

        documents = []

        for index, row in df.iterrows():

            resume_text = str(row["Resume_str"])

            category = str(row["Category"])

            chunks = self.text_splitter.split_text(

                resume_text

            )

            for chunk_number, chunk in enumerate(chunks):

                doc = {

                    "id": f"{index}_{chunk_number}",

                    "category": category,

                    "content": chunk

                }

                documents.append(doc)

        print(f"Created {len(documents)} chunks.\n")

        return documents

    def ingest(self):

        resumes = self.create_documents()

        vector_db = VectorStore()

        vector_db.create_db(resumes)

        print("\nRAG Database Created Successfully!\n")


if __name__ == "__main__":

    pipeline = ResumeIngestion()

    pipeline.ingest()