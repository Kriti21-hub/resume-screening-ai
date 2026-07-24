import streamlit as st
import fitz

from utils.skill_extractor import extract_skills
from utils.similarity import calculate_score

st.set_page_config(page_title="Resume Screening AI")

st.title("📄 Resume Screening AI")

resume = st.file_uploader("Upload your Resume (PDF)", type="pdf")

job_description = st.text_area("📋 Paste Job Description")

if resume:

    pdf = fitz.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    st.subheader("📃 Extracted Resume Text")
    st.write(text)

    st.subheader("🛠 Skills Found")

    skills = extract_skills(text)

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")

    if job_description:

        score, matched_skills, missing_skills = calculate_score(text, job_description)

        st.subheader("📊 ATS Match Score")

        st.progress(int(score))

        st.write(f"## {score}% Match")

        st.subheader("✅ Matching Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.warning("No matching skills found.")

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills!")