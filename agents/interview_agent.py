"""
-------------------------------------------------------
Interview Agent
-------------------------------------------------------
Generates personalized interview questions
using Gemini.

Author : AI Recruitment Bot Team
"""

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from prompts.interview_prompt import INTERVIEW_PROMPT

load_dotenv()


class InterviewAgent:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_NAME"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.3
        )

        self.prompt = PromptTemplate(
            template=INTERVIEW_PROMPT,
            input_variables=[
                "matched_skills",
                "missing_skills",
                "ats_score",
                "strengths",
                "weaknesses"
            ]
        )

        self.parser = JsonOutputParser()

    def generate_questions(
        self,
        matched_skills,
        missing_skills,
        ats_score,
        strengths,
        weaknesses
    ):

        try:

            chain = (
                self.prompt
                | self.llm
                | self.parser
            )

            response = chain.invoke(
                {
                    "matched_skills": matched_skills,
                    "missing_skills": missing_skills,
                    "ats_score": ats_score,
                    "strengths": strengths,
                    "weaknesses": weaknesses
                }
            )

            return response

        except Exception as e:

            return {
                "technical_questions": [],
                "scenario_questions": [],
                "hr_questions": [],
                "error": str(e)
            }


if __name__ == "__main__":

    matched_skills = [
        "Python",
        "SQL",
        "Machine Learning"
    ]

    missing_skills = [
        "Docker",
        "AWS"
    ]

    strengths = [
        "Strong Python knowledge",
        "Good ML Projects"
    ]

    weaknesses = [
        "No cloud deployment experience"
    ]

    ats_score = 82

    agent = InterviewAgent()

    result = agent.generate_questions(
        matched_skills,
        missing_skills,
        ats_score,
        strengths,
        weaknesses
    )

    print(result)