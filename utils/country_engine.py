
COUNTRY_FORMATS = {
    "usa": {
        "name": "United States",
        "sections": ["Contact", "Professional Summary", "Work Experience", "Education", "Skills", "Certifications"],
        "style": "reverse_chronological",
        "photo_required": False,
        "page_limit": 1,
        "tips": [
            "Keep it to 1 page for entry-level, 2 pages for experienced.",
            "Use action verbs and quantify achievements.",
            "No photo needed.",
            "Include LinkedIn URL."
        ]
    },
    "uk": {
        "name": "United Kingdom",
        "sections": ["Contact", "Personal Statement", "Work Experience", "Education", "Skills", "References"],
        "style": "reverse_chronological",
        "photo_required": False,
        "page_limit": 2,
        "tips": [
            "No photo required (anti-discrimination laws).",
            "Include GCSEs and A-Levels if relevant.",
            "Keep to 2 pages max.",
            "Mention right to work status if applicable."
        ]
    },
    "canada": {
        "name": "Canada",
        "sections": ["Contact", "Professional Summary", "Work Experience", "Education", "Skills", "Languages"],
        "style": "reverse_chronological",
        "photo_required": False,
        "page_limit": 2,
        "tips": [
            "Bilingual resume (English/French) is a plus.",
            "No photo needed.",
            "Highlight Canadian experience if you have it.",
            "Include SIN only if explicitly asked."
        ]
    },
    "australia": {
        "name": "Australia",
        "sections": ["Contact", "Career Objective", "Work Experience", "Education", "Skills", "Referees"],
        "style": "reverse_chronological",
        "photo_required": False,
        "page_limit": 2,
        "tips": [
            "Use 'Referees' instead of 'References'.",
            "No photo required.",
            "Highlight relevant Australian experience.",
            "Keep to 2-3 pages."
        ]
    },
    "germany": {
        "name": "Germany",
        "sections": ["Personal Details", "Photo", "Education", "Work Experience", "Skills", "Languages"],
        "style": "tabular",
        "photo_required": True,
        "page_limit": 2,
        "tips": [
            "Photo is required (passport size, professional).",
            "Include date of birth and nationality (standard in Germany).",
            "Use formal language.",
            "Keep to 1-2 pages."
        ]
    },
    "france": {
        "name": "France",
        "sections": ["Personal Info", "Photo", "Formation", "Expérience Professionnelle", "Compétences", "Langues"],
        "style": "reverse_chronological",
        "photo_required": True,
        "page_limit": 2,
        "tips": [
            "Photo is commonly included (passport size).",
            "CV is called 'CV' or 'Curriculum Vitae'.",
            "Mention language proficiency clearly.",
            "Keep to 1-2 pages."
        ]
    },
    "india": {
        "name": "India",
        "sections": ["Contact", "Career Objective", "Academic Qualifications", "Work Experience", "Skills", "Projects", "Personal Details"],
        "style": "reverse_chronological",
        "photo_required": True,
        "page_limit": 2,
        "tips": [
            "Passport size photo is required.",
            "Include percentage/CGPA for academics.",
            "Mention hobbies and interests.",
            "Keep to 1-2 pages."
        ]
    },
    "uae": {
        "name": "United Arab Emirates",
        "sections": ["Contact", "Professional Summary", "Work Experience", "Education", "Skills", "Languages", "Visa Status"],
        "style": "reverse_chronological",
        "photo_required": True,
        "page_limit": 2,
        "tips": [
            "Passport size photo is preferred.",
            "Mention visa status clearly.",
            "Highlight Arabic language skills if any.",
            "Keep to 1-2 pages."
        ]
    }
}

def get_country_format(country_code):
    return COUNTRY_FORMATS.get(country_code.lower(), COUNTRY_FORMATS["usa"])

def get_all_countries():
    return COUNTRY_FORMATS
