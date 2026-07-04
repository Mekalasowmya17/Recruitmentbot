import streamlit as st
from graph.workflow import app

st.title("AI Recruitment Bot")

resume = st.text_area("Paste Resume")

jd = st.text_area("Paste Job Description")

if st.button("Evaluate Candidate"):

    state = {
        "resume": resume,
        "job_description": jd,
        "score": "",
        "interview_questions": "",
        "decision": ""
    }

    result = app.invoke(state)

    st.subheader("Resume Score")

    st.write(result["score"])

    st.subheader("Interview Questions")

    st.write(result["interview_questions"])

    st.subheader("Decision")

    st.write(result["decision"])