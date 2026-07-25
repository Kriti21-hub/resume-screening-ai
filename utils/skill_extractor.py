# List of technical skills to detect
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
    "Data Visualization",
    "Streamlit",
    "OpenCV",
    "Keras",
    "Flask",
    "Django",
    "AWS",
    "Azure",
    "Google Cloud",
    "Linux",
    "HTML",
    "CSS",
    "JavaScript",
    "Java",
    "C++",
    "C",
    "Power BI",
    "Tableau",
    "Excel",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "REST API",
    "NLP",
    "Computer Vision",
    "Data Science",
    "Artificial Intelligence",
    "Statistics",
    "Matplotlib",
    "Seaborn"
]


def extract_skills(text):
    """
    Extracts technical skills from the given text.
    Returns a list of unique detected skills.
    """

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    # Remove duplicates while preserving order
    unique_skills = list(dict.fromkeys(found_skills))

    return unique_skills