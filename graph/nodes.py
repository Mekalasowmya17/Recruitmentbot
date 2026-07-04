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
    """

    score = agent.ask(prompt)

    state["score"] = score

    return state


def generate_questions(state):

    prompt = f"""
    Resume:
    {state['resume']}

    Generate 5 interview questions.
    """

    questions = agent.ask(prompt)

    state["interview_questions"] = questions

    return state


def final_decision(state):

    prompt = f"""
    Resume Score:

    {state['score']}

    Decide:

    Shortlist

    or

    Reject

    Give reason.
    """

    decision = agent.ask(prompt)

    state["decision"] = decision

    return state