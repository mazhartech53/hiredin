
MIGRATION_MAP = {
    "usa": {
        "canada": ["Add bilingual skills", "Mention Canadian experience", "Remove photo"],
        "uk": ["Change 'Resume' to 'CV'", "Remove photo", "Add GCSEs/A-Levels"],
        "australia": ["Change 'References' to 'Referees'", "Remove photo", "Mention visa status"],
        "uae": ["Add visa status", "Add photo", "Mention nationality"]
    },
    "uk": {
        "usa": ["Change 'CV' to 'Resume'", "Add LinkedIn URL", "Quantify achievements"],
        "canada": ["Add bilingual skills", "Mention right to work", "Remove photo"],
        "australia": ["Change 'References' to 'Referees'", "Mention visa status"],
        "uae": ["Add photo", "Mention nationality", "Add visa status"]
    },
    "canada": {
        "usa": ["Add LinkedIn URL", "Quantify achievements", "Remove photo"],
        "uk": ["Change 'Resume' to 'CV'", "Remove photo", "Add GCSEs/A-Levels"],
        "australia": ["Change 'References' to 'Referees'", "Mention visa status"],
        "uae": ["Add photo", "Mention nationality", "Add visa status"]
    },
    "australia": {
        "usa": ["Add LinkedIn URL", "Quantify achievements", "Remove photo"],
        "uk": ["Change 'Resume' to 'CV'", "Remove photo", "Add GCSEs/A-Levels"],
        "canada": ["Add bilingual skills", "Mention right to work", "Remove photo"],
        "uae": ["Add photo", "Mention nationality", "Add visa status"]
    },
    "germany": {
        "usa": ["Remove photo", "Remove DOB/nationality", "Add LinkedIn URL"],
        "uk": ["Remove photo", "Remove DOB/nationality", "Change 'Lebenslauf' to 'CV'"],
        "canada": ["Remove photo", "Remove DOB/nationality", "Add bilingual skills"],
        "france": ["Change 'Lebenslauf' to 'CV'", "Keep photo", "Switch to French format"]
    },
    "france": {
        "usa": ["Remove photo", "Add LinkedIn URL", "Quantify achievements"],
        "uk": ["Remove photo", "Change 'CV' to 'CV' (same)", "Add GCSEs/A-Levels"],
        "canada": ["Add bilingual skills", "Remove photo"],
        "germany": ["Change 'CV' to 'Lebenslauf'", "Keep photo", "Add DOB/nationality"]
    },
    "india": {
        "usa": ["Remove photo", "Remove personal details", "Add LinkedIn URL"],
        "uk": ["Remove photo", "Remove personal details", "Change 'Resume' to 'CV'"],
        "canada": ["Remove photo", "Remove personal details", "Add bilingual skills"],
        "uae": ["Keep photo", "Add visa status", "Mention nationality"]
    },
    "uae": {
        "usa": ["Remove photo", "Remove nationality", "Add LinkedIn URL"],
        "uk": ["Remove photo", "Remove nationality", "Change 'Resume' to 'CV'"],
        "canada": ["Remove photo", "Remove nationality", "Add bilingual skills"],
        "india": ["Keep photo", "Keep nationality", "Add personal details"]
    }
}

def get_migration_steps(from_country, to_country):
    key = f"{from_country.lower()}_{to_country.lower()}"
    steps = MIGRATION_MAP.get(from_country.lower(), {}).get(to_country.lower(), [])
    if not steps:
        return ["Review target country format", "Adjust sections accordingly", "Tailor content for local standards"]
    return steps
