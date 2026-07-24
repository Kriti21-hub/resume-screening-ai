import streamlit as st
import fitz
from utils.skill_extractor import extract_skills

st.title("📄 Resume Screening AI")

resume = st.file_uploader("Upload your Resume", type="pdf")

if resume:

    st.success("✅ Resume Uploaded Successfully!")

    pdf = fitz.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    st.subheader("Extracted Resume Text")
    st.text(text)

    st.subheader("🛠 Skills Found")

    found_skills = extract_skills(text)

    if found_skills:
        for skill in found_skills:
            st.markdown(f"✅ {skill}")
    else:
        st.warning("No skills found.")