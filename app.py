import streamlit as st
import fitz
import plotly.express as px

from utils.feedback import generate_feedback
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_score


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Resume Screening & ATS Analyzer",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 AI Resume Screening & ATS Analyzer")

st.markdown("""
Welcome! 👋

Upload your **Resume (PDF)** and paste a **Job Description** to:

- 📄 Extract Resume Text
- 🛠 Detect Technical Skills
- 📊 Calculate ATS Match Score
- ✅ View Matching Skills
- ❌ Identify Missing Skills
- 📈 Visualize Skill Match
- 💡 Get Resume Improvement Suggestions
""")

st.divider()

# --------------------------------------------------
# Inputs
# --------------------------------------------------
resume = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "📋 Paste Job Description"
)

# --------------------------------------------------
# Main Program
# --------------------------------------------------
if resume:

    # Extract text from PDF
    pdf = fitz.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    # --------------------------------------------------
    # Resume Text
    # --------------------------------------------------
    st.header("📃 Extracted Resume")

    st.write(text)

    st.divider()

    # --------------------------------------------------
    # Skills
    # --------------------------------------------------
    st.header("🛠 Skills Detected")

    skills = extract_skills(text)

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")

    # --------------------------------------------------
    # ATS Analysis
    # --------------------------------------------------
    if job_description.strip():

        score, matched_skills, missing_skills = calculate_score(
            text,
            job_description
        )

        st.divider()

        st.header("📊 ATS Analysis")

        st.progress(int(score))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🎯 ATS Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "✅ Matched Skills",
                len(matched_skills)
            )

        with col3:
            st.metric(
                "❌ Missing Skills",
                len(missing_skills)
            )

        # --------------------------------------------------
        # Matching Skills
        # --------------------------------------------------
        st.divider()

        st.subheader("✅ Matching Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.info("No matching skills found.")

        # --------------------------------------------------
        # Missing Skills
        # --------------------------------------------------
        st.divider()

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills!")

        # --------------------------------------------------
        # Pie Chart
        # --------------------------------------------------
        st.divider()

        st.header("📈 Skill Match Visualization")

        fig = px.pie(
            names=["Matched Skills", "Missing Skills"],
            values=[
                len(matched_skills),
                len(missing_skills)
            ],
            hole=0.5,
            title="Resume Skill Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # --------------------------------------------------
        # Resume Suggestions
        # --------------------------------------------------
        st.divider()

        st.header("💡 Resume Improvement Suggestions")

        if score == 100:

            st.success(
                "🎉 Excellent! Your resume perfectly matches the required technical skills."
            )

            st.balloons()

        else:

            if missing_skills:

                for skill in missing_skills:

                    st.info(
                        f"Consider adding **{skill}** to your resume if you have practical experience with it."
                    )

            st.warning(
                "Only include skills that you genuinely know. Never add skills just to improve your ATS score."
            )

        # --------------------------------------------------
        # AI Resume Feedback
        # --------------------------------------------------
        st.divider()

        st.header("🤖 AI Resume Feedback")

        feedback = generate_feedback(
            score,
            matched_skills,
            missing_skills
        )

        st.text(feedback)