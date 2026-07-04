"""
=========================================================
PDF Reader Utility
=========================================================

Reads one or more PDF resumes and extracts plain text.

Author : AI Recruitment Bot
Module : RAG Pipeline
"""

import os
from typing import List, Dict
from pypdf import PdfReader


class PDFReader:
    """
    Utility class for reading PDF resumes.
    """

    def __init__(self):
        pass

    def read_pdf(self, pdf_path: str) -> str:
        """
        Reads a single PDF and extracts all text.

        Args:
            pdf_path (str): Path to PDF file

        Returns:
            str: Extracted text
        """

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(
                f"PDF file not found: {pdf_path}"
            )

        try:

            reader = PdfReader(pdf_path)

            extracted_text = ""

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

            return extracted_text.strip()

        except Exception as e:
            raise Exception(
                f"Error reading PDF {pdf_path}: {str(e)}"
            )

    def read_all_pdfs(self, folder_path: str) -> List[Dict]:
        """
        Reads every PDF inside a folder.

        Args:
            folder_path (str)

        Returns:
            List[Dict]
        """

        if not os.path.exists(folder_path):
            raise FileNotFoundError(
                f"Folder not found: {folder_path}"
            )

        documents = []

        pdf_files = [
            file
            for file in os.listdir(folder_path)
            if file.lower().endswith(".pdf")
        ]

        if len(pdf_files) == 0:
            print("No PDF resumes found.")
            return documents

        for pdf in pdf_files:

            path = os.path.join(folder_path, pdf)

            try:

                text = self.read_pdf(path)

                documents.append({
                    "file_name": pdf,
                    "file_path": path,
                    "content": text
                })

            except Exception as e:

                print(f"Skipping {pdf}")

                print(e)

        return documents


if __name__ == "__main__":

    reader = PDFReader()

    docs = reader.read_all_pdfs("data/resumes")

    print("=" * 70)

    print(f"Loaded {len(docs)} resumes")

    print("=" * 70)

    for doc in docs:

        print()

        print("File :", doc["file_name"])

        print()

        print(doc["content"][:500])

        print("-" * 70)