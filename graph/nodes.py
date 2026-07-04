from agents.coordinator_agent import CoordinatorAgent

agent = CoordinatorAgent()


def resume_screening(state):

    prompt = f"""
    You are an HR recruiter.

    Resume:
    {state['resume']}

    Job Description:
    {state['job_description']}

    Give only a suitability score out of 100.
    Return only the number.
    """

    score = agent.ask(prompt)

    state["score"] = score

    return state


def generate_questions(state):

    prompt = f"""
    Resume:
    {state['resume']}

    Generate 5 interview questions for this candidate.
    """

    questions = agent.ask(prompt)

    state["interview_questions"] = questions

    return state


def final_decision(state):

    prompt = f"""
    Resume Score:
    {state['score']}

    Based on the score, decide one of the following:

    - Shortlist
    - Reject

    Give a short reason.
    """

    decision = agent.ask(prompt)

    state["decision"] = decision

    return state


def salary_evaluation(state):

    prompt = f"""
    You are an HR Salary Expert.

    Analyze the resume below and estimate the expected annual salary in India.

    Resume:
    {state['resume']}

    Return ONLY the salary in LPA.

    Example outputs:
    4 LPA
    6 LPA
    8 LPA
    12 LPA
    18 LPA
    """

    salary = agent.ask(prompt)

    print("Gemini Salary Response:", salary)

    state["average_salary"] = salary


    return state