import streamlit as st
from matcher import analyze_match

st.set_page_config(page_title="Resume Job Matcher", page_icon="📄", layout="wide")

st.title("📄 Resume–Job Description Matcher")
st.write("Compare a resume with a job description using TF-IDF similarity and skill matching.")

st.info("Tip: Paste the text from your resume and the target job description below. This app runs locally and does not send your text to an external AI API.")

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "📄 Resume text",
        height=420,
        placeholder="Paste your resume text here..."
    )

with col2:
    job_text = st.text_area(
        "💼 Job description",
        height=420,
        placeholder="Paste the job description here..."
    )

if st.button("🔍 Analyze Match", type="primary", use_container_width=True):
    if not resume_text.strip() or not job_text.strip():
        st.warning("Please provide both the resume text and job description.")
    else:
        result = analyze_match(resume_text, job_text)

        st.subheader("📊 Match Result")
        st.metric("Resume Match", f"{result['match_percentage']:.1f}%")

        left, right = st.columns(2)

        with left:
            st.markdown("### ✅ Matching skills")
            if result["matching_skills"]:
                for skill in result["matching_skills"]:
                    st.write(f"✓ {skill}")
            else:
                st.write("No skills from the built-in list were detected in both texts.")

        with right:
            st.markdown("### ❌ Missing skills")
            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.write(f"• {skill}")
            else:
                st.write("No missing skills from the detected job-skill list.")

        st.markdown("### 🔑 Skills detected in the job description")
        if result["job_skills"]:
            st.write(", ".join(result["job_skills"]))
        else:
            st.write("No skills from the built-in skill list were detected.")

        st.caption(
            "The percentage is a text-similarity score, not a hiring prediction. "
            "Skill matching uses a predefined beginner-friendly skill list."
        )
