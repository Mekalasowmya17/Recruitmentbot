"""
=========================================================
RAG Agent
=========================================================

Uses:
1. ChromaDB Retriever
2. Gemini
3. Resume Ranking

Author : AI Recruitment Bot
"""

import os
from dotenv import load_dotenv
from google import genai

from rag.retriever import ResumeRetriever

load_dotenv()


class RAGAgent:

    def __init__(self):

        api_key = os.getenv("GEMINI_API")

        if not api_key:
            raise ValueError("GEMINI_API not found.")

        self.client = genai.Client(
            api_key=api_key
        )

        self.retriever = ResumeRetriever()

    def retrieve_candidates(self, job_description):

        documents = self.retriever.search(

            query=job_description,

            k=5

        )

        context = ""

        for i, doc in enumerate(documents, start=1):

            context += f"""

Candidate {i}

Category:
{doc.metadata.get("category")}

Resume:

{doc.page_content}

"""

        return context

    def analyze_candidates(self, job_description):

        context = self.retrieve_candidates(job_description)

        prompt = f"""
You are an expert AI Recruitment Assistant.

Job Description:

{job_description}

Below are the most relevant candidate resumes.

{context}

Perform the following:

1. Rank candidates.

2. Give Match Score out of 100.

3. Mention strengths.

4. Mention weaknesses.

5. Mention missing skills.

6. Recommend Hire / Maybe Hire / Reject.

Return the result in a neat format.
"""

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text


if __name__ == "__main__":

    agent = RAGAgent()

    job = input("Enter Job Description : ")

    result = agent.analyze_candidates(job)

    print()

    print("=" * 80)

    print(result)

    print("=" * 80)