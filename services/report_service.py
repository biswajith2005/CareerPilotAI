from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def generate_resume_report(analysis):
    """
    Generate a PDF report for the resume analysis.
    Returns PDF bytes.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>CareerPilot AI - Resume Analysis Report</b>", styles["Title"]))
    elements.append(Paragraph(f"<b>ATS Score:</b> {analysis.ats_score}", styles["Heading2"]))

    elements.append(Paragraph("<b>Strengths</b>", styles["Heading2"]))
    for item in analysis.strengths:
        elements.append(Paragraph(f"• {item}", styles["BodyText"]))

    elements.append(Paragraph("<b>Weaknesses</b>", styles["Heading2"]))
    for item in analysis.weaknesses:
        elements.append(Paragraph(f"• {item}", styles["BodyText"]))

    elements.append(Paragraph("<b>Suggestions</b>", styles["Heading2"]))
    for item in analysis.suggestions:
        elements.append(Paragraph(f"• {item}", styles["BodyText"]))

    document.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf