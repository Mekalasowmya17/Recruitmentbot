from langgraph.graph import StateGraph, END
from graph.state import RecruitmentState
from graph.nodes import (
    resume_screening,
    generate_questions,
    final_decision,
    salary_evaluation,
)

workflow = StateGraph(RecruitmentState)

workflow.add_node("Screen Resume", resume_screening)
workflow.add_node("Generate Questions", generate_questions)
workflow.add_node("Decision", final_decision)
workflow.add_node("Salary Evaluation", salary_evaluation)

workflow.set_entry_point("Screen Resume")

workflow.add_edge("Screen Resume", "Generate Questions")
workflow.add_edge("Generate Questions", "Decision")
workflow.add_edge("Decision", "Salary Evaluation")
workflow.add_edge("Salary Evaluation", END)

app = workflow.compile()