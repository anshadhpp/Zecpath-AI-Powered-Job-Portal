"""Screening questions (PRD Phase 5) and simple answer parsing."""
import re

SCREENING_QUESTIONS = [
    "Please introduce yourself.",
    "What is your educational qualification?",
    "How many years of total experience do you have?",
    "What are your relevant skills?",
    "What is your current location?",
    "What is your notice period?",
    "What is your expected salary?",
]


def extract_notice_period_days(answer: str) -> int | None:
    """Convert answers like '30 days', '2 months', 'immediate' to days."""
    text = answer.lower()
    if "immediate" in text:
        return 0
    match = re.search(r"(\d+)\s*(day|week|month)", text)
    if not match:
        return None
    factor = {"day": 1, "week": 7, "month": 30}[match.group(2)]
    return int(match.group(1)) * factor