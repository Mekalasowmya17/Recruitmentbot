"""
-------------------------------------------------------
Salary Agent
-------------------------------------------------------
Uses SalaryTool to fetch salary benchmarks
and returns structured JSON.

Author : AI Recruitment Bot Team
"""

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from tools.salary_tool import SalaryTool

load_dotenv()


SALARY_PROMPT = """
You are an AI Recruitment Salary Expert.

Based on the salary benchmark below, generate a structured report.

Salary Benchmark:
{salary_report}

Candidate Details:
Role: {job_role}
Experience: {experience} years
Location: {location}
Skills: {skills}

Return ONLY valid JSON in this format:

{{
    "average_salary": "",
    "salary_range": "",
    "market_demand": "",
    "top_companies": [],
    "recommended_skills": [],
    "summary": ""
}}

Do not return markdown.
Return only JSON.
"""


class SalaryAgent:

    def __init__(self):

        self.salary_tool = SalaryTool()

        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_NAME", "gemini-2.5-flash"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2
        )

        self.prompt = PromptTemplate(
            template=SALARY_PROMPT,
            input_variables=[
                "salary_report",
                "job_role",
                "experience",
                "location",
                "skills"
            ]
        )

        self.parser = JsonOutputParser()

    def analyze_salary(
        self,
        job_role: str,
        location: str,
        experience: int,
        skills: list
    ) -> dict:

        try:

            benchmark = self.salary_tool.get_salary_data(
                job_role=job_role,
                location=location,
                experience=experience,
                skills=skills
            )

            chain = (
                self.prompt
                | self.llm
                | self.parser
            )

            result = chain.invoke(
                {
                    "salary_report": benchmark["salary_report"],
                    "job_role": job_role,
                    "experience": experience,
                    "location": location,
                    "skills": ", ".join(skills)
                }
            )

            return result

        except Exception as e:

            return {
                "average_salary": "Unavailable",
                "salary_range": "Unavailable",
                "market_demand": "Unknown",
                "top_companies": [],
                "recommended_skills": [],
                "summary": str(e)
            }


if __name__ == "__main__":

    agent = SalaryAgent()

    response = agent.analyze_salary(
        job_role="Machine Learning Engineer",
        location="Hyderabad",
        experience=2,
        skills=[
            "Python",
            "Machine Learning",
            "SQL",
            "TensorFlow"
        ]
    )

    print(response)