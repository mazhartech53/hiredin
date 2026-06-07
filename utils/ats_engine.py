
import re

ATS_KEYWORDS = {
    "software engineer": ["python", "java", "javascript", "git", "agile", "sql", "docker", "aws"],
    "data scientist": ["python", "r", "machine learning", "sql", "pandas", "numpy", "statistics"],
    "product manager": ["agile", "scrum", "roadmap", "stakeholder", "jira", "analytics"],
    "marketing": ["seo", "google analytics", "social media", "content", "campaign", "crm"],
    "sales": ["crm", "lead generation", "negotiation", "closing", "b2b", "quota"],
    "hr": ["recruitment", "onboarding", "payroll", "compliance", "talent acquisition"],
    "finance": ["accounting", "excel", "financial analysis", "budgeting", "forecasting"],
    "teacher": ["curriculum", "lesson planning", "classroom management", "assessment"],
    "nurse": ["patient care", "clinical", "medication", "emergency", "cpr"],
    "designer": ["photoshop", "illustrator", "figma", "ui/ux", "branding"]
}

COMMON_ACTION_VERBS = [
    "achieved", "improved", "trained", "managed", "created", "resolved",
    "volunteered", "influenced", "increased", "decreased", "launched",
    "revenue", "profits", "under budget", "won", "awarded", "promoted"
]

def analyze_ats_score(resume_text, job_title=""):
    score = 0
    feedback = []

    # Check for keywords
    resume_lower = resume_text.lower()
    keywords = ATS_KEYWORDS.get(job_title.lower(), ["python", "management", "communication", "leadership"])
    found_keywords = [k for k in keywords if k in resume_lower]
    keyword_score = min(len(found_keywords) / len(keywords) * 40, 40)
    score += keyword_score

    if len(found_keywords) < 3:
        feedback.append(f"Add more industry keywords like: {', '.join([k for k in keywords if k not in found_keywords][:3])}")

    # Check for action verbs
    found_verbs = [v for v in COMMON_ACTION_VERBS if v in resume_lower]
    verb_score = min(len(found_verbs) / 5 * 20, 20)
    score += verb_score

    if len(found_verbs) < 3:
        feedback.append("Use more action verbs (achieved, improved, managed, created).")

    # Check formatting issues
    if len(re.findall(r'[^\x00-\x7F]', resume_text)) > 0:
        feedback.append("Remove special characters that ATS may not read.")
        score -= 5

    if "table" in resume_lower:
        feedback.append("Avoid using tables — ATS struggles to read them.")
        score -= 10

    # Check contact info
    if not re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resume_text):
        feedback.append("Add a valid email address.")
        score -= 5

    # Check length
    word_count = len(resume_text.split())
    if word_count < 150:
        feedback.append("Resume is too short. Aim for 300-500 words.")
        score -= 10
    elif word_count > 800:
        feedback.append("Resume is too long. Keep it concise.")
        score -= 5

    # Check for quantifiable achievements
    numbers = re.findall(r'\d+%|\d+\s*(million|billion|thousand|lakhs|crores)?', resume_lower)
    if len(numbers) < 2:
        feedback.append("Add quantifiable achievements (e.g., 'Increased sales by 20%').")
    else:
        score += 10

    score = max(0, min(100, score + 30))  # Base score

    return {
        "score": round(score),
        "feedback": feedback,
        "found_keywords": found_keywords,
        "word_count": word_count
    }
