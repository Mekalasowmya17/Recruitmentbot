"""
=========================================================
Retriever
=========================================================

Retrieves the most relevant resumes using semantic search.

Author : AI Recruitment Bot
"""

from rag.vector_store import VectorStore


class ResumeRetriever:

    def __init__(self):

        self.vector_store = VectorStore()

        self.db = self.vector_store.load_db()

    def search(self, query, k=5):
        """
        Search similar resumes.

        Args:
            query (str)
            k (int)

        Returns:
            list
        """

        results = self.db.similarity_search(

            query,

            k=k

        )

        return results

    def print_results(self, results):

        print("\n")

        print("=" * 70)

        print("Top Matching Candidates")

        print("=" * 70)

        for i, doc in enumerate(results, start=1):

            print(f"\nCandidate {i}")

            print("-" * 60)

            print("Category :", doc.metadata["category"])

            print()

            print(doc.page_content[:500])

            print("\n")


if __name__ == "__main__":

    retriever = ResumeRetriever()

    query = input("Enter Job Requirement : ")

    results = retriever.search(query)

    retriever.print_results(results)