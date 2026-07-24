import streamlit as st
import fitz

st.title("📄 Resume Screening AI")

resume = st.file_uploader("Upload your Resume", type="pdf")

if resume is not None:

    st.success("✅ Resume Uploaded Successfully!")

    pdf = fitz.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    st.subheader("Extracted Resume Text")

    st.text(text)