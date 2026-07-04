"""
-------------------------------------------------------
Recommendation Agent
-------------------------------------------------------
Generates the final hiring recommendation using Gemini.

Author : AI Recruitment Bot Team
"""

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from prompts.recommendation_prompt import RECOMMENDATION_PROMPT

load_dotenv()


class RecommendationAgent:
    """
    Generates the final hiring recommendation.
    """

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_NAME"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2
        )

        self.prompt = PromptTemplate(
            template=RECOMMENDATION_PROMPT,
            input_variables=[
                "ats_score",
                "matched_skills",
                "missing_skills",
                "strengths",
                "weaknesses",
                "interview_questions",
                "salary"
            ]
        )

        self.parser = JsonOutputParser()

    def generate_recommendation(
        self,
        ats_score,
        matched_skills,
        missing_skills,
        strengths,
        weaknesses,
        interview_questions,
        salary
    ):
        """
        Generate final hiring recommendation.

        Returns:
            dict
        """

        try:

            chain = (
                self.prompt
                | self.llm
                | self.parser
            )

            result = chain.invoke(
                {
                    "ats_score": ats_score,
                    "matched_skills": matched_skills,
                    "missing_skills": missing_skills,
                    "strengths": strengths,
                    "weaknesses": weaknesses,
                    "interview_questions": interview_questions,
                    "salary": salary
                }
            )

            return result

        except Exception as e:

            return {
                "recommendation": "Error",
                "confidence_score": 0,
                "summary": "Unable to generate recommendation.",
                "strengths": [],
                "weaknesses": [],
                "learning_roadmap": [],
                "reason": str(e)
            }


if __name__ == "__main__":

    matched_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas"
    ]

    missing_skills = [
        "Docker",
        "AWS"
    ]

    strengths = [
        "Strong Python skills",
        "Excellent ML projects"
    ]

    weaknesses = [
        "Limited cloud experience"
    ]

    interview_questions = {
        "technical_questions": [
            "Explain Python decorators.",
            "Difference between CNN and RNN."
        ],
        "scenario_questions": [
            "How would you optimize a slow ML model?"
        ],
        "hr_questions": [
            "Tell me about yourself."
        ]
    }

    salary = "₹8–10 LPA"

    agent = RecommendationAgent()

    response = agent.generate_recommendation(
        ats_score=86,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        strengths=strengths,
        weaknesses=weaknesses,
        interview_questions=interview_questions,
        salary=salary
    )

    print(response)