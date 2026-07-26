from io import BytesIO
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def generate_pdf(score, matched_skills, missing_skills, feedback):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle("ATS Report")

    y = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(180, y, "ATS Resume Analysis Report")

    y -= 40

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, f"ATS Score: {score}%")

    y -= 40

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Matched Skills")

    y -= 25

    pdf.setFont("Helvetica", 12)

    for skill in matched_skills:
        pdf.drawString(70, y, f"• {skill}")
        y -= 20

    y -= 20

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Missing Skills")

    y -= 25

    pdf.setFont("Helvetica", 12)

    for skill in missing_skills:
        pdf.drawString(70, y, f"• {skill}")
        y -= 20

    y -= 20

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "AI Feedback")

    y -= 25

    pdf.setFont("Helvetica", 11)

    for line in feedback.split("\n"):
        pdf.drawString(50, y, line)
        y -= 18

    pdf.save()

    buffer.seek(0)

    return buffer