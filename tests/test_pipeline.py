import pytest

from ats_engine.matcher import JobRequirements, ats_score, shortlist
from interview_ai.question_engine import build_question_plan, difficulty_for_experience
from parsers.resume_parser import ParsedResume, parse_resume_file
from scoring.aggregator import aggregate, decide
from screening_ai.questions import SCREENING_QUESTIONS, extract_notice_period_days

SAMPLE = "data/samples/sample_resume.txt"


def test_parser():
    r = parse_resume_file(SAMPLE)
    assert r.email == "asha.nair@example.com"
    assert {"react", "node.js", "mongodb"} <= set(r.skills)
    assert r.experience_years == 3


def test_ats_full_match():
    job = JobRequirements("MERN", ["React", "Node.js", "MongoDB", "Express"], 2)
    score = ats_score(parse_resume_file(SAMPLE), job)
    assert score == 100.0 and shortlist(score)


def test_ats_no_match():
    job = JobRequirements("Java Dev", ["java", "docker"], 5)
    assert not shortlist(ats_score(ParsedResume(), job))


def test_screening():
    assert len(SCREENING_QUESTIONS) == 7
    assert extract_notice_period_days("2 months") == 60
    assert extract_notice_period_days("immediate") == 0
    assert extract_notice_period_days("unsure") is None


def test_interview_plan():
    assert difficulty_for_experience(1) == "basic"
    assert build_question_plan("MERN", 6)["difficulty"] == "advanced"


def test_scoring():
    final = aggregate({"ats": 80, "hr": 70, "technical": 90, "machine_test": 60})
    assert final == 76.5
    assert decide(final) == "selected"
    assert decide(55) == "hold"
    assert decide(20) == "rejected"
    with pytest.raises(ValueError):
        aggregate({"unknown": 1})