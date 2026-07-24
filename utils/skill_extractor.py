from utils.skill_extractor import extract_skills
st.text(text)
st.subheader("Skills Found")

skills = extract_skills(text)

if skills:
    for skill in skills:
        st.success(skill)
else:
    st.warning("No skills found.")