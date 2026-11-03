"""Role-based resume scoring (PRD Phase 2)."""
from dataclasses import dataclass

from parsers.resume_parser import ParsedResume
from utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class JobRequirements:
    title: str
    required_skills: list[str]
    min_experience: float = 0.0


def ats_score(resume: ParsedResume, job: JobRequirements) -> float:
    """Score 0-100: 70% skill match, 30% experience fit."""
    required = {s.lower() for s in job.required_skills}
    skill_part = len(required & set(resume.skills)) / len(required) if required else 1.0
    if job.min_experience > 0:
        exp_part = min(resume.experience_years / job.min_experience, 1.0)
    else:
        exp_part = 1.0
    score = round(100 * (0.7 * skill_part + 0.3 * exp_part), 2)
    logger.info("ATS score for %s: %s", job.title, score)
    return score


def shortlist(score: float, cutoff: float = 60.0) -> bool:
    return score >= cutoff