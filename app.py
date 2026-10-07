import streamlit as st
from matcher import analyze_match


def format_skill(skill):
    special_cases = {
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "api": "API",
        "nlp": "NLP",
        "aws": "AWS",
        "azure": "Azure",
        "ai agents": "AI Agents",
        "llm": "LLM",
        "mlops": "MLOps",
        "oops": "OOPs",
    }

    return special_cases.get(skill.lower(), skill.title())

st.set_page_config(
    page_title="AI Resume–JD Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume–Job Description Matcher")

st.write(
    "Compare a resume with a job description using NLP-based "
    "text similarity and skill matching."
)

st.info(
    "💡 This application uses TF-IDF, cosine similarity, and "
    "skill matching to generate a resume–JD matching score. "
    "It runs locally and does not send your resume data to an external AI API."
)
# Sample data for quick testing
sample_resume = """
Vaishnavi R
Computer Engineering Graduate

Skills:
Java, Python, SQL, MySQL, HTML, CSS, JavaScript,
Machine Learning, Pandas, NumPy, Scikit-learn,
Git, GitHub, Data Analysis, Communication,
Problem Solving

Projects:
Big Mart Sales Prediction using Machine Learning.
Developed a predictive analysis project using Python,
Pandas, NumPy and Scikit-learn.

Online Railway Reservation System using Java,
JDBC and MySQL.
"""

sample_job = """
Computational Science Associate

We are looking for an entry-level professional with
knowledge of Python, Java, SQL, data analysis,
machine learning and problem solving.

Required Skills:
Python, Java, SQL, Machine Learning, Data Structures,
Algorithms, Communication and Problem Solving.

Knowledge of Django, data analysis and software
development concepts is preferred.
"""

if st.button("📋 Load Sample Data"):
    st.session_state["resume_text"] = sample_resume
    st.session_state["job_text"] = sample_job

if st.button("🧹 Clear"):
    st.session_state["resume_text"] = ""
    st.session_state["job_text"] = ""
    st.rerun()
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "📄 Resume Text",
        value=st.session_state.get("resume_text", ""),
        height=420,
        placeholder="Paste your resume text here..."
    )

with col2:
    job_text = st.text_area(
        "💼 Job Description",
        value=st.session_state.get("job_text", ""),
        height=420,
        placeholder="Paste the target job description here..."
    )

if st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if not resume_text.strip() or not job_text.strip():

        st.warning(
            "⚠️ Please provide both your resume and the job description."
        )

    else:

        result = analyze_match(
            resume_text,
            job_text
        )

        st.subheader("📊 Resume–JD Match Analysis")

        score1, score2, score3 = st.columns(3)
        st.progress(
             int(result["skill_match"]),
              text=f"Skill Coverage: {result['skill_match']:.1f}%"
              )

        with score1:
            st.metric(
                "🎯 Overall Match",
                f"{result['match_percentage']:.1f}%"
            )

        with score2:
            st.metric(
                "📝 Content Similarity",
                f"{result['content_similarity']:.1f}%"
            )

        with score3:
            st.metric(
                "🛠️ Skill Match",
                f"{result['skill_match']:.1f}%"
            )

        st.divider()

        left, right = st.columns(2)

        with left:

            st.markdown("### ✅ Matching Skills")

            if result["matching_skills"]:

                for skill in result["matching_skills"]:
                    st.success(format_skill(skill))

            else:

                st.write(
                    "No matching skills were detected."
                )

        with right:

            st.markdown("### ❌ Missing Skills")

            if result["missing_skills"]:

                for skill in result["missing_skills"]:
                    st.warning(f"• {skill.title()}")

            else:

                st.write(
                    "No missing skills were detected."
                )

        st.divider()

        st.markdown("### 💪 Resume Strengths")

        if result["matching_skills"]:
            st.write(
                "Your resume contains several skills relevant to this job:"
            )

            for skill in result["matching_skills"]:
                st.success(f"✓ {format_skill(skill)}")
        else:
            st.write(
                "No matching skills were detected from the predefined skill list."
            )

        st.markdown("### 📌 Areas to Improve")

        if result["missing_skills"]:
            st.write(
                "Consider highlighting or developing these job-relevant skills:"
            )

            for skill in result["missing_skills"]:
                st.warning(f"• {skill.title()}")

        else:
            st.success(
                "Your resume covers all detected job skills."
            )

        st.markdown(
            "### 🔑 Skills Detected in Job Description"
        )

        if result["job_skills"]:

           st.write(
    ", ".join(format_skill(skill) for skill in result["job_skills"])
)

        else:

            st.write(
                "No skills from the predefined skill list were detected."
            )

        st.divider()

        st.markdown("### 💡 How the Score Is Calculated")

        st.write(
            "Overall Match = 60% Content Similarity + 40% Skill Match"
        )

        st.caption(
            "This is a custom resume–job description matching score "
            "for analysis purposes. It is not an official ATS score "
            "or a hiring prediction."
        )