from rapidfuzz import process, fuzz
SKILLS = [
    "python", "sql", "excel", "power bi", "tableau",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "docker", "git", "airflow", "dbt", "aws", "gcp",
    "nlp", "time series", "forecasting", "mlops", "fastapi",
    "azure", "kubernetes", "statistics", "machine learning",
]

def match_skills(text: str, limit=10, score_cutoff=80):
    if not isinstance(text, str):
        return []
    matches = process.extract(
        text.lower(),
        SKILLS,
        scorer=fuzz.partial_ratio,
        limit=limit
    )
    return [m[0] for m in matches if m[1] >= score_cutoff]