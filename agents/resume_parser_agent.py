"""
=========================================================
Resume Parser Agent
=========================================================

Uses Gemini to extract structured information
from resumes.

Author : AI Recruitment Bot
"""

import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()


class ResumeParserAgent:

    def __init__(self):

        api_key = os.getenv("GEMINI_API")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def parse_resume(self, resume_text):

        prompt = f"""
You are an expert AI Resume Parser.

Extract the following information.

Return ONLY valid JSON.

{{
"name":"",
"email":"",
"phone":"",
"skills":[],
"education":[],
"experience":[],
"projects":[],
"certifications":[],
"summary":""
}}

Resume:

{resume_text}

"""

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)


if __name__ == "__main__":

    sample_resume = """

John Doe

Python Developer

Email : john@gmail.com

Phone : 9999999999

Skills

Python

Machine Learning

TensorFlow

SQL

Education

B.Tech Computer Science

Experience

Software Engineer - ABC Pvt Ltd

Projects

AI Recruitment Bot

"""

    parser = ResumeParserAgent()

    result = parser.parse_resume(sample_resume)

    print(json.dumps(result, indent=4))