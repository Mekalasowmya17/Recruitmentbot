"""
-------------------------------------------------------
Salary Tool
-------------------------------------------------------
Uses WebSearchTool to fetch salary benchmarks
and returns structured salary information.

Author : AI Recruitment Bot Team
"""

from tools.web_search import WebSearchTool


class SalaryTool:
    """
    Salary Benchmark Tool
    """

    def __init__(self):
        self.web_search = WebSearchTool()

    def get_salary_data(
        self,
        job_role: str,
        location: str,
        experience: int,
        skills: list
    ) -> dict:
        """
        Fetch salary benchmark.

        Args:
            job_role (str)
            location (str)
            experience (int)
            skills (list)

        Returns:
            dict
        """

        skills_text = ", ".join(skills)

        query = f"""
Find the latest salary benchmark for:

Job Role: {job_role}
Location: {location}
Experience: {experience} years

Candidate Skills:
{skills_text}

Return:
1. Average Salary
2. Salary Range
3. Top Hiring Companies
4. Market Demand
5. Trending Skills
"""

        result = self.web_search.search(query)

        return {
            "job_role": job_role,
            "location": location,
            "experience": experience,
            "skills": skills,
            "salary_report": result
        }


if __name__ == "__main__":

    tool = SalaryTool()

    response = tool.get_salary_data(
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