from utils.skill_extractor import extract_skills

def calculate_score(resume_text, job_text):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2), matched_skills, missing_skills