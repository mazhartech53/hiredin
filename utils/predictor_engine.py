
import re

REJECTION_FACTORS = {
    "short_resume": {
        "check": lambda text: len(text.split()) < 150,
        "message": "Resume is too short (under 150 words). Recruiters may reject it.",
        "severity": "high"
    },
    "no_contact": {
        "check": lambda text: not re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text),
        "message": "No valid email address found. This is a critical omission.",
        "severity": "high"
    },
    "no_phone": {
        "check": lambda text: not re.search(r'[\+]?[0-9\s\-\(\)]{7,}', text),
        "message": "No phone number found. Recruiters need a way to contact you.",
        "severity": "high"
    },
    "passive_language": {
        "check": lambda text: any(w in text.lower() for w in ["was responsible", "were involved", "is managed", "are tasked"]),
        "message": "Too much passive voice. Use active voice with strong action verbs.",
        "severity": "medium"
    },
    "weak_phrases": {
        "check": lambda text: any(w in text.lower() for w in ["responsible for", "duties included", "worked on", "helped with"]),
        "message": "Contains weak phrases. Replace with strong action verbs and quantified results.",
        "severity": "medium"
    },
    "spelling_errors": {
        "check": lambda text: any(w in text.lower() for w in ["teh", "recieve", "seperate", "definately", "occured"]),
        "message": "Spelling errors detected. Proofread carefully before submitting.",
        "severity": "high"
    },
    "no_quantifiable": {
        "check": lambda text: len(re.findall(r'\d+%|\d+\s*(million|billion|thousand|lakhs|crores)?', text.lower())) < 2,
        "message": "No quantifiable achievements. Add numbers to show impact (e.g., 'Increased sales by 20%').",
        "severity": "medium"
    },
    "too_long": {
        "check": lambda text: len(text.split()) > 800,
        "message": "Resume is too long (over 800 words). Keep it concise and relevant.",
        "severity": "low"
    },
    "personal_info": {
        "check": lambda text: re.search(r'\b(married|single|divorced|age|dob|date of birth|religion|caste)\b', text.lower()),
        "message": "Personal information included. This may lead to discrimination.",
        "severity": "medium"
    },
    "missing_skills": {
        "check": lambda text: "skills" not in text.lower(),
        "message": "No dedicated skills section. Add a clear skills section.",
        "severity": "medium"
    }
}

def analyze_rejection_risk(resume_text):
    risks = []
    score = 100

    for factor_name, factor_data in REJECTION_FACTORS.items():
        if factor_data["check"](resume_text):
            risks.append({
                "factor": factor_name,
                "message": factor_data["message"],
                "severity": factor_data["severity"]
            })
            if factor_data["severity"] == "high":
                score -= 15
            elif factor_data["severity"] == "medium":
                score -= 8
            else:
                score -= 3

    score = max(0, min(100, score))

    # Risk level
    if score >= 80:
        risk_level = "Low"
        color = "green"
    elif score >= 50:
        risk_level = "Medium"
        color = "orange"
    else:
        risk_level = "High"
        color = "red"

    return {
        "score": score,
        "risk_level": risk_level,
        "color": color,
        "risks": risks
    }
