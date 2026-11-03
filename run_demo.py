from ats_engine.matcher import JobRequirements, ats_score, shortlist
from interview_ai.question_engine import build_question_plan
from parsers.resume_parser import parse_resume_file
from scoring.aggregator import aggregate, decide
from screening_ai.questions import SCREENING_QUESTIONS

resume = parse_resume_file("data/samples/sample_resume.txt")
job = JobRequirements("MERN Stack Developer", ["React", "Node.js", "MongoDB", "Express"], 2)

ats = ats_score(resume, job)
print("Parsed resume:", resume)
print("ATS score:", ats, "| shortlisted:", shortlist(ats))

if shortlist(ats):
    print("Screening questions:", len(SCREENING_QUESTIONS))
    print("Interview plan:", build_question_plan(job.title, resume.experience_years))
    final = aggregate({"ats": ats, "hr": 70, "technical": 80})
    print("Final score:", final, "->", decide(final))