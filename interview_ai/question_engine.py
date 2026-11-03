"""Experience-based question planning (PRD Phases 15 and 37)."""


def difficulty_for_experience(years: float) -> str:
    if years < 2:
        return "basic"
    if years < 5:
        return "intermediate"
    return "advanced"


def build_question_plan(role: str, years: float, num_questions: int = 5) -> dict:
    return {
        "role": role,
        "difficulty": difficulty_for_experience(years),
        "num_questions": num_questions,
    }