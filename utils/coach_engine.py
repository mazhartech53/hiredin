
COUNTRY_COACH_TIPS = {
    "usa": {
        "title": "US Resume Best Practices",
        "tips": [
            "Use a clean, professional format with clear headings.",
            "Quantify achievements with numbers (e.g., 'Increased sales by 25%').",
            "Tailor your resume for each job application.",
            "Include a LinkedIn profile URL.",
            "Use reverse chronological order for work experience.",
            "Avoid including a photo (can lead to discrimination concerns).",
            "Use standard fonts: Arial, Calibri, or Times New Roman (10-12pt).",
            "Save as PDF to preserve formatting."
        ]
    },
    "uk": {
        "title": "UK CV Best Practices",
        "tips": [
            "Use 'CV' not 'Resume' in the UK.",
            "Include a brief personal statement at the top.",
            "Mention GCSEs and A-Levels if relevant.",
            "Do NOT include a photo (strict anti-discrimination laws).",
            "Keep to 2 pages maximum.",
            "Mention right to work status if applicable.",
            "Use British spelling (e.g., 'organise' not 'organize').",
            "Include hobbies only if relevant to the role."
        ]
    },
    "canada": {
        "title": "Canadian Resume Best Practices",
        "tips": [
            "Bilingual resume (English/French) is a major advantage.",
            "Highlight Canadian work experience if you have it.",
            "Do NOT include a photo.",
            "Mention language proficiency clearly.",
            "Include SIN only if explicitly requested.",
            "Use Canadian spelling conventions.",
            "Keep to 1-2 pages.",
            "Tailor for each job posting."
        ]
    },
    "australia": {
        "title": "Australian Resume Best Practices",
        "tips": [
            "Use 'Referees' instead of 'References'.",
            "Do NOT include a photo.",
            "Highlight relevant Australian experience.",
            "Keep to 2-3 pages maximum.",
            "Include a career objective for entry-level roles.",
            "Mention visa status if on a work visa.",
            "Use Australian spelling (e.g., 'organisation').",
            "Include relevant certifications and licenses."
        ]
    },
    "germany": {
        "title": "German Lebenslauf Best Practices",
        "tips": [
            "Photo is REQUIRED — use a professional passport-size photo.",
            "Include date of birth and nationality (standard practice).",
            "Use formal, polite language.",
            "Keep to 1-2 pages.",
            "Include 'Lebenslauf' as the heading.",
            "List education BEFORE work experience.",
            "Sign and date the CV at the bottom.",
            "Include language proficiency levels (A1-C2)."
        ]
    },
    "france": {
        "title": "French CV Best Practices",
        "tips": [
            "Photo is commonly included (passport size, professional).",
            "Use 'CV' or 'Curriculum Vitae' as heading.",
            "Keep to 1-2 pages.",
            "Mention language proficiency clearly (CEFR levels).",
            "Include ' centres d\'intérêt' (hobbies/interests).",
            "Use formal French if applying in French.",
            "List education in reverse chronological order.",
            "Include a brief 'Accroche' (hook) at the top."
        ]
    },
    "india": {
        "title": "Indian Resume Best Practices",
        "tips": [
            "Passport size photo is REQUIRED in most cases.",
            "Include percentage/CGPA for all academic qualifications.",
            "Mention personal details: Date of Birth, Gender, Marital Status, Languages.",
            "Keep to 1-2 pages.",
            "Include a career objective.",
            "Mention hobbies and interests.",
            "Include projects and internships prominently.",
            "Use a clean, tabular format."
        ]
    },
    "uae": {
        "title": "UAE Resume Best Practices",
        "tips": [
            "Passport size photo is preferred.",
            "Mention visa status clearly (e.g., 'Visit Visa', 'Employment Visa').",
            "Highlight Arabic language skills if any.",
            "Keep to 1-2 pages.",
            "Include nationality (common practice in UAE).",
            "Mention driving license if relevant.",
            "Use a professional, clean format.",
            "Tailor for each employer."
        ]
    }
}

def get_country_coach(country_code):
    return COUNTRY_COACH_TIPS.get(country_code.lower(), COUNTRY_COACH_TIPS["usa"])
