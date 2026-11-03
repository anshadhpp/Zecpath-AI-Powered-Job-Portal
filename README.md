# Zecpath AI

AI engine for **Zecpath, an AI-powered job portal and automated hiring assistant**.
It covers resume screening (ATS), AI screening calls, interview intelligence and
candidate scoring, following the Zecpath Product Requirements Document (PRD).

## Features

- **Resume parsing:** extracts email, skills, experience and education from TXT, PDF and DOCX files
- **ATS scoring:** ranks resumes against a job's required skills and experience (0-100) and shortlists candidates
- **Screening:** the standard PRD screening questions plus answer parsing (for example, notice period in days)
- **Interview planning:** picks question difficulty from years of experience
- **Score aggregation:** combines ATS, HR, technical and machine-test scores into a final decision (selected, hold or rejected)
- **Activity logging:** a shared logger that records AI activity to `logs/app.log`

## Tech stack

Python 3.10+, pytest, pdfplumber, python-docx, python-dotenv

## Project layout

```
Zecpath-AI-Powered-Job-Portal/
├── data/            # raw/, processed/, samples/ (sample data only)
├── parsers/         # resume parsing
├── ats_engine/      # resume scoring and shortlisting
├── screening_ai/    # screening questions and answer analysis
├── interview_ai/    # interview question planning
├── scoring/         # score aggregation and decisions
├── utils/           # shared helpers, including logging
├── tests/           # automated tests (pytest)
├── logs/            # runtime logs (not committed to Git)
├── docs/            # code standards and documentation
├── run_demo.py      # end-to-end demo of the pipeline
├── pytest.ini
└── requirements.txt
```

| Folder | Purpose | PRD phases |
|---|---|---|
| `parsers/` | Resume parsing (PDF, DOCX, TXT) | 2 |
| `ats_engine/` | Resume scoring and shortlisting | 2, 3 |
| `screening_ai/` | Screening questions and answer analysis | 5 |
| `interview_ai/` | Interview question generation | 15, 37 |
| `scoring/` | Score aggregation and hiring decisions | 20, 45, 70 |
| `utils/` | Logging and shared helpers | all |

## Quick start

**1. Clone the repository**
```bash
git clone https://github.com/anshadhpp/Zecpath-AI-Powered-Job-Portal.git
cd Zecpath-AI-Powered-Job-Portal
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the tests and the demo**
```bash
pytest
python run_demo.py
```

## Usage example

```python
from parsers.resume_parser import parse_resume_file
from ats_engine.matcher import JobRequirements, ats_score, shortlist
from scoring.aggregator import aggregate, decide

resume = parse_resume_file("data/samples/sample_resume.txt")
job = JobRequirements("MERN Stack Developer", ["React", "Node.js", "MongoDB"], min_experience=2)

score = ats_score(resume, job)
print(score, shortlist(score))        # 100.0 True

final = aggregate({"ats": score, "hr": 70, "technical": 80})
print(decide(final))                  # selected
```

## Logging

Use the shared logger instead of `print()`:

```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Resume parsed")
```

Logs are printed to the console and saved to `logs/app.log` (rotating file, 5 MB x 3 backups).

## Testing

```bash
pytest
```

Tests live in `tests/`. Every new function should come with a test.

## Code standards

See [docs/CODE_STANDARDS.md](docs/CODE_STANDARDS.md) for the full rules: PEP 8 style,
Google-style docstrings, Git branching, commit message format, and testing and logging conventions.

Git workflow:
- Branches: `main` (stable), `dev` (integration), `feature/<name>`
- Commit messages: `feat(ats): add keyword matcher`, `fix(parser): handle empty PDF`, `docs:`, `test:`

## Roadmap

- [x] Repository structure, logging and test setup (Day 3)
- [ ] spaCy-based skill and entity extraction
- [ ] Bias-reduced ATS scoring
- [ ] LLM-driven adaptive interview questions
- [ ] Speech-to-text answer analysis
- [ ] Communication and aptitude scoring

## Author

Anshad P P
