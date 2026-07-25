def generate_feedback(score, matched_skills, missing_skills):

    feedback = []

    feedback.append(f"🎯 ATS Score: {score}%")

    if score >= 90:
        feedback.append("Excellent resume! It closely matches the job requirements.")
    elif score >= 70:
        feedback.append("Good resume. A few improvements can significantly increase your ATS score.")
    elif score >= 50:
        feedback.append("Average match. Consider improving your technical skills section.")
    else:
        feedback.append("Low ATS match. Your resume needs more relevant technical skills.")

    feedback.append("")
    feedback.append("✅ Strengths")

    if matched_skills:
        for skill in matched_skills:
            feedback.append(f"• {skill}")
    else:
        feedback.append("• No matching skills found.")

    feedback.append("")
    feedback.append("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            feedback.append(f"• {skill}")
    else:
        feedback.append("• None")

    return "\n".join(feedback)