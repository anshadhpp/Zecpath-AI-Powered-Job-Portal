"""Resume parsing (PRD Phase 2): extract email, skills, experience, education."""
import re
from dataclasses import dataclass, field
from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)

SKILL_VOCAB = {
    "python", "java", "javascript", "react", "node.js", "mongodb", "express",
    "sql", "postgresql", "docker", "aws", "git", "figma", "machine learning",
}
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
EXP_RE = re.compile(r"(\d+(?:\.\d+)?)\+?\s*years?", re.IGNORECASE)
EDU_RE = re.compile(r"\b(b\.?tech|m\.?tech|b\.?sc|m\.?sc|mba|bca|mca|ph\.?d)\b", re.IGNORECASE)


@dataclass
class ParsedResume:
    email: str | None = None
    skills: list[str] = field(default_factory=list)
    experience_years: float = 0.0
    education: list[str] = field(default_factory=list)


def read_text(path: str | Path) -> str:
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        import pdfplumber

        with pdfplumber.open(path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    if suffix == ".docx":
        import docx

        return "\n".join(p.text for p in docx.Document(path).paragraphs)
    return path.read_text(encoding="utf-8")


def parse_resume_text(text: str) -> ParsedResume:
    lower = text.lower()
    email = EMAIL_RE.search(text)
    skills = sorted(
        s for s in SKILL_VOCAB if re.search(rf"(?<!\w){re.escape(s)}(?!\w)", lower)
    )
    years = [float(y) for y in EXP_RE.findall(text)]
    education = sorted({m.group(0).upper() for m in EDU_RE.finditer(text)})
    result = ParsedResume(
        email=email.group(0) if email else None,
        skills=skills,
        experience_years=max(years, default=0.0),
        education=education,
    )
    logger.info("Resume parsed: %d skills, %.1f years", len(skills), result.experience_years)
    return result


def parse_resume_file(path: str | Path) -> ParsedResume:
    return parse_resume_text(read_text(path))