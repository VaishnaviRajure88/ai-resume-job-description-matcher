import re
from typing import List, Dict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Skills used for resume and job-description analysis.
SKILLS = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "html", "css", "react", "node.js", "flask", "django",
    "sql", "mysql", "postgresql", "mongodb",
    "pandas", "numpy", "matplotlib", "scikit-learn",
    "machine learning", "artificial intelligence",
    "predictive modeling", "data science", "data analysis",
    "deep learning", "nlp", "natural language processing",
    "tensorflow", "pytorch",
    "llm", "large language models", "ai agents",
    "mlops", "machine learning architecture",
    "git", "github", "docker", "aws", "azure",
    "linux", "rest api", "api",
    "excel", "power bi", "tableau",
    "data visualization",
    "communication", "problem solving",
    "data structures", "algorithms", "oops",
    "object oriented programming"
]


def clean_text(text: str) -> str:
    """Normalize text while keeping useful technical terms."""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def contains_skill(text: str, skill: str) -> bool:
    """Check whether a skill appears in the text."""
    text = clean_text(text)
    skill = skill.lower()

    # Use word boundaries for simple words.
    if re.fullmatch(r"[a-z0-9]+", skill):
        return bool(re.search(rf"\b{re.escape(skill)}\b", text))

    # For terms containing punctuation or spaces,
    # use a substring check.
    return skill in text


def extract_skills(text: str) -> List[str]:
    """Return skills from the predefined skill list found in the text."""
    return [skill for skill in SKILLS if contains_skill(text, skill)]


def calculate_similarity(resume_text: str, job_text: str) -> float:
    """Calculate TF-IDF cosine similarity."""
    documents = [
        clean_text(resume_text),
        clean_text(job_text)
    ]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return float(score)


def calculate_skill_match(
    matching_skills: List[str],
    job_skills: List[str]
) -> float:
    """Calculate percentage of detected job skills present in the resume."""

    if not job_skills:
        return 0.0

    return (len(matching_skills) / len(job_skills)) * 100


def analyze_match(resume_text: str, job_text: str) -> Dict:
    """Analyze resume and job description similarity and skills."""

    # Calculate text similarity.
    similarity = calculate_similarity(
        resume_text,
        job_text
    )

    content_similarity = similarity * 100

    # Extract skills.
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    # Compare skills.
    matching_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills.difference(resume_skills)
    )

    # Calculate skill match percentage.
    skill_match = calculate_skill_match(
        matching_skills,
        list(job_skills)
    )

    # Combine content similarity and skill coverage.
    overall_match = (
        content_similarity * 0.60
        + skill_match * 0.40
    )

    return {
        "match_percentage": overall_match,
        "content_similarity": content_similarity,
        "skill_match": skill_match,
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
    }