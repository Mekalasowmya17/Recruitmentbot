"""
--------------------------------------------------
Web Search Utility
--------------------------------------------------
Used for searching salary information
and market trends.

Author : AI Recruitment Bot Team
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class WebSearchTool:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_NAME"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )

    def search(self, query: str) -> str:
        """
        Search salary information.

        Args:
            query (str)

        Returns:
            str
        """

        prompt = f"""
You are an AI recruitment assistant.

Search and summarize the following information:

{query}

Provide:
1. Average Salary
2. Salary Range
3. Current Market Demand
4. Important Skills

Keep the answer concise.
"""

        response = self.llm.invoke(prompt)

        return response.content


if __name__ == "__main__":

    tool = WebSearchTool()

    result = tool.search(
        "Python Machine Learning Engineer salary in Hyderabad"
    )

    print(result)