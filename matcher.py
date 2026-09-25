import re
from typing import List, Dict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Beginner-friendly skill dictionary.
# Add more skills here as you encounter them in job descriptions.
SKILLS = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "html", "css", "react", "node.js", "flask", "django",
    "sql", "mysql", "postgresql", "mongodb",
    "pandas", "numpy", "matplotlib", "scikit-learn",
    "machine learning", "deep learning", "nlp",
    "tensorflow", "pytorch",
    "git", "github", "docker", "aws", "azure",
    "linux", "rest api", "api",
    "excel", "power bi", "tableau",
    "data analysis", "data visualization",
    "communication", "problem solving",
    "data structures", "algorithms", "oops"
]


def clean_text(text: str) -> str:
    """Normalize text while keeping useful technical terms."""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def contains_skill(text: str, skill: str) -> bool:
    """Check whether a skill appears in text."""
    text = clean_text(text)
    skill = skill.lower()

    # Use word boundaries for simple words.
    # For terms containing punctuation/spaces, a normal substring check is safer.
    if re.fullmatch(r"[a-z0-9]+", skill):
        return bool(re.search(rf"\b{re.escape(skill)}\b", text))

    return skill in text


def extract_skills(text: str) -> List[str]:
    """Return skills from the predefined skill list that occur in the text."""
    return [skill for skill in SKILLS if contains_skill(text, skill)]


def calculate_similarity(resume_text: str, job_text: str) -> float:
    """Calculate TF-IDF cosine similarity between resume and job description."""
    documents = [clean_text(resume_text), clean_text(job_text)]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return float(score)


def analyze_match(resume_text: str, job_text: str) -> Dict:
    """Return the similarity score and skill comparison."""
    similarity = calculate_similarity(resume_text, job_text)

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    matching_skills = sorted(resume_skills.intersection(job_skills))
    missing_skills = sorted(job_skills.difference(resume_skills))

    return {
        "match_percentage": similarity * 100,
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
    }
