skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NumPy",
    "Pandas",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Git",
    "GitHub",
    "Docker",
    "FastAPI",
    "Data Visualization"
]

def extract_skills(text):
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills