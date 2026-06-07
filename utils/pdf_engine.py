
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from io import BytesIO
import os

def generate_pdf(resume_data, country_code="usa", photo_path=None):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1a365d'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c5282'),
        spaceAfter=6,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY
    )

    contact_style = ParagraphStyle(
        'CustomContact',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#4a5568')
    )

    story = []

    # Photo (if provided and country requires it)
    if photo_path and os.path.exists(photo_path):
        try:
            img = Image(photo_path, width=1.2*inch, height=1.5*inch)
            story.append(img)
            story.append(Spacer(1, 6))
        except:
            pass

    # Name
    name = resume_data.get("name", "Your Name")
    story.append(Paragraph(name, title_style))

    # Contact info
    contact_parts = []
    if resume_data.get("email"):
        contact_parts.append(resume_data["email"])
    if resume_data.get("phone"):
        contact_parts.append(resume_data["phone"])
    if resume_data.get("location"):
        contact_parts.append(resume_data["location"])
    if resume_data.get("linkedin"):
        contact_parts.append(resume_data["linkedin"])

    if contact_parts:
        story.append(Paragraph(" | ".join(contact_parts), contact_style))
        story.append(Spacer(1, 12))

    # Professional Summary
    if resume_data.get("summary"):
        story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
        story.append(Paragraph(resume_data["summary"], normal_style))

    # Work Experience
    if resume_data.get("experience"):
        story.append(Paragraph("WORK EXPERIENCE", heading_style))
        for exp in resume_data["experience"]:
            exp_text = f"<b>{exp.get('title', '')}</b> — {exp.get('company', '')}"
            if exp.get('duration'):
                exp_text += f" ({exp.get('duration', '')})"
            story.append(Paragraph(exp_text, normal_style))
            if exp.get('description'):
                story.append(Paragraph(exp.get('description', ''), normal_style))
            story.append(Spacer(1, 6))

    # Education
    if resume_data.get("education"):
        story.append(Paragraph("EDUCATION", heading_style))
        for edu in resume_data["education"]:
            edu_text = f"<b>{edu.get('degree', '')}</b> — {edu.get('institution', '')}"
            if edu.get('year'):
                edu_text += f" ({edu.get('year', '')})"
            story.append(Paragraph(edu_text, normal_style))
            if edu.get('details'):
                story.append(Paragraph(edu.get('details', ''), normal_style))
            story.append(Spacer(1, 6))

    # Skills
    if resume_data.get("skills"):
        story.append(Paragraph("SKILLS", heading_style))
        skills_text = ", ".join(resume_data["skills"]) if isinstance(resume_data["skills"], list) else resume_data["skills"]
        story.append(Paragraph(skills_text, normal_style))

    # Certifications
    if resume_data.get("certifications"):
        story.append(Paragraph("CERTIFICATIONS", heading_style))
        for cert in resume_data["certifications"]:
            story.append(Paragraph(f"• {cert}", normal_style))

    # Projects
    if resume_data.get("projects"):
        story.append(Paragraph("PROJECTS", heading_style))
        for proj in resume_data["projects"]:
            proj_text = f"<b>{proj.get('name', '')}</b>"
            if proj.get('description'):
                proj_text += f" — {proj.get('description', '')}"
            story.append(Paragraph(proj_text, normal_style))
            story.append(Spacer(1, 6))

    # Languages
    if resume_data.get("languages"):
        story.append(Paragraph("LANGUAGES", heading_style))
        langs = resume_data["languages"]
        if isinstance(langs, list):
            story.append(Paragraph(", ".join([f"{l.get('name','')} ({l.get('level','')})" for l in langs]), normal_style))
        else:
            story.append(Paragraph(str(langs), normal_style))

    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
