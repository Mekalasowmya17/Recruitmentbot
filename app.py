import re
import streamlit as st
from pypdf import PdfReader

from graph.workflow import app

st.set_page_config(
    page_title="AI Recruitment Bot",
    page_icon="🤖",
    layout="wide"
)


def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


st.title("🤖 AI Recruitment Bot")

st.write("Upload a Resume and enter the Job Description.")

st.divider()

resume_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "📋 Job Description",
    height=250
)


if st.button("🚀 Evaluate Candidate"):

    if resume_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please enter the Job Description.")
        st.stop()

    resume_text = extract_text(resume_file)

    with st.spinner("Analyzing Candidate..."):

        result = app.invoke(
            {
                "resume": resume_text,
                "job_description": job_description
            }
        )

    st.success("✅ Evaluation Completed")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Resume",
        "Interview",
        "Decision",
        "Salary",
        "Raw Output"
    ]
)

    with tab1:

        st.subheader("Resume")

        st.text(result.get("resume", ""))

        st.subheader("Job Description")

        st.write(result.get("job_description", ""))

        score = result.get("score", "N/A")

        st.metric(
            label="ATS Score",
            value=score
        )

    with tab2:

        st.subheader("Interview Questions")

        questions = result.get("interview_questions", "")

        if isinstance(questions, list):

            for i, q in enumerate(questions, start=1):
                st.write(f"**{i}.** {q}")

        else:
            st.write(questions)

    with tab3:

        st.subheader("Hiring Decision")

        decision = result.get("decision", "No Decision")

        if "hire" in decision.lower():
            st.success(decision)

        elif "shortlist" in decision.lower():
            st.info(decision)

        else:
            st.warning(decision)

    with tab4:

        st.subheader("💰 Salary & HR Evaluation")

        market_salary = result.get("average_salary")

        if market_salary is None or market_salary == "":
            market_salary = "Not Available"

        st.write("### Expected Market Salary")
        st.success(market_salary)

        expected_salary = st.number_input(
            "Candidate Expected Salary (LPA)",
            min_value=1.0,
            max_value=100.0,
            step=0.5
        )

        nums = re.findall(r"\d+\.?\d*", str(market_salary))

        if nums:
            company_salary = float(nums[0])
        else:
            company_salary = 10.0

        if st.button("Evaluate Salary"):

            if expected_salary <= company_salary:

                st.success("✅ Salary expectation is acceptable.")
                st.balloons()

                st.info("""
### Final Recommendation

✔ Candidate Selected

✔ Proceed to Human HR Evaluation

✔ Generate Offer Letter
""")

            elif expected_salary <= company_salary + 2:

                st.warning("⚠ Salary expectation is slightly higher.")

                st.info("""
### Recommendation

Proceed to Human HR Evaluation

Salary Negotiation Required
""")

            else:

                st.error("❌ Salary expectation is much higher than company benchmark.")

                st.warning("""
### Recommendation

Manager Approval Required

Candidate can still be considered after discussion.
""")
    with tab5:

        st.subheader("Raw Output")
        st.json(result)