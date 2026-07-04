"""
Skill Match Agent

Compares candidate resume with Job Description
using Gemini and returns structured JSON.
"""

import json
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.matching_prompt import MATCHING_PROMPT

load_dotenv()


class SkillMatchAgent:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_NAME"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2
        )

        self.parser = JsonOutputParser()

        self.prompt = PromptTemplate(
            template=MATCHING_PROMPT,
            input_variables=[
                "resume",
                "job_description"
            ]
        )

    def match_skills(
        self,
        resume: str,
        job_description: str
    ) -> dict:

        try:

            chain = (
                self.prompt
                | self.llm
                | self.parser
            )

            result = chain.invoke(
                {
                    "resume": resume,
                    "job_description": job_description
                }
            )

            return result

        except Exception as e:

            return {
                "matched_skills": [],
                "missing_skills": [],
                "ats_score": 0,
                "strengths": [],
                "weaknesses": [],
                "improvement_suggestions": [],
                "error": str(e)
            }


if __name__ == "__main__":

    resume = """
    Python
    SQL
    Machine Learning
    Deep Learning
    Streamlit
    """

    jd = """
    Looking for Python Developer

    Skills:

    Python
    SQL
    Docker
    AWS
    Machine Learning
    """

    agent = SkillMatchAgent()

    response = agent.match_skills(
        resume,
        jd
    )

    print(json.dumps(response, indent=4))