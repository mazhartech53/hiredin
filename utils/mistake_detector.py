
import re

COMMON_MISTAKES = {
    "spelling": [
        ("teh", "the"), ("recieve", "receive"), ("seperate", "separate"),
        ("definately", "definitely"), ("occured", "occurred"), ("accomodate", "accommodate"),
        ("acheive", "achieve"), ("begining", "beginning"), ("beleive", "believe"),
        ("calender", "calendar"), ("collegue", "colleague"), ("concious", "conscious"),
        ("existance", "existence"), ("foriegn", "foreign"), ("goverment", "government"),
        ("harrass", "harass"), ("independant", "independent"), ("liason", "liaison"),
        ("maintainance", "maintenance"), ("neccessary", "necessary"), ("noticable", "noticeable"),
        ("occurance", "occurrence"), ("paralell", "parallel"), ("persistant", "persistent"),
        ("posession", "possession"), ("preceeding", "preceding"), ("priviledge", "privilege"),
        ("publically", "publicly"), ("recomend", "recommend"), ("refering", "referring"),
        ("relevent", "relevant"), ("religous", "religious"), ("repetion", "repetition"),
        ("sieze", "seize"), ("succesful", "successful"), ("supercede", "supersede"),
        ("suprise", "surprise"), ("tommorow", "tomorrow"), ("untill", "until"),
        ("weild", "wield"), ("wich", "which"), ("yourslef", "yourself")
    ],
    "grammar": [
        ("i am", "I am"), ("i have", "I have"), ("i will", "I will"),
        ("dont", "don\'t"), ("wont", "won\'t"), ("cant", "can\'t"),
        ("isnt", "isn\'t"), ("wasnt", "wasn\'t"), ("didnt", "didn\'t"),
        ("hasnt", "hasn\'t"), ("havent", "haven\'t"), ("shouldnt", "shouldn\'t"),
        ("wouldnt", "wouldn\'t"), ("couldnt", "couldn\'t")
    ]
}

PROFESSIONAL_MISTAKES = [
    "responsible for", "duties included", "worked on", "helped with",
    "assisted in", "participated in", "involved in"
]

def detect_mistakes(resume_text):
    mistakes = []
    text_lower = resume_text.lower()

    # Spelling mistakes
    for wrong, correct in COMMON_MISTAKES["spelling"]:
        if wrong in text_lower:
            mistakes.append({
                "type": "spelling",
                "issue": f"'\'{wrong}\'' should be '\'{correct}\''",
                "severity": "high"
            })

    # Grammar mistakes
    for wrong, correct in COMMON_MISTAKES["grammar"]:
        if wrong in text_lower:
            mistakes.append({
                "type": "grammar",
                "issue": f"'\'{wrong}\'' should be '\'{correct}\''",
                "severity": "medium"
            })

    # Weak phrases
    for phrase in PROFESSIONAL_MISTAKES:
        if phrase in text_lower:
            mistakes.append({
                "type": "professional",
                "issue": f"Replace '\'{phrase}\'' with a strong action verb.",
                "severity": "medium"
            })

    # Check for personal info
    if re.search(r'\b(married|single|divorced|age|dob|date of birth|religion|caste)\b', text_lower):
        mistakes.append({
            "type": "privacy",
            "issue": "Avoid including personal details like marital status, age, or religion.",
            "severity": "high"
        })

    # Check for passive voice indicators
    passive_indicators = ["was responsible", "were involved", "is managed", "are tasked"]
    for indicator in passive_indicators:
        if indicator in text_lower:
            mistakes.append({
                "type": "style",
                "issue": f"Avoid passive voice: '\'{indicator}\''. Use active voice instead.",
                "severity": "low"
            })

    return mistakes
