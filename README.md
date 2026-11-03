# Zecpath AI

AI engine for the Zecpath AI-powered job portal: resume screening (ATS),
AI screening calls, interview intelligence and candidate scoring.

## Project layout

| Folder | Purpose |
|---|---|
| `data/` | Raw, processed and sample data |
| `parsers/` | Resume parsing (PDF, DOCX, TXT) |
| `ats_engine/` | Resume scoring and shortlisting |
| `screening_ai/` | Screening questions and answer analysis |
| `interview_ai/` | Interview question generation |
| `scoring/` | Score aggregation and hiring decisions |
| `utils/` | Shared helpers, including logging |
| `tests/` | Automated tests (pytest) |
| `logs/` | Runtime logs (not committed to Git) |
| `docs/` | Code standards and documentation |

## Setup

1. Clone the repository:
   git clone https://github.com/<your-username>/zecpath-ai.git
   cd zecpath-ai

2. Create and activate a virtual environment (Windows):
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

## Logging

Use the shared logger instead of print():

    from utils.logger import get_logger
    logger = get_logger(__name__)
    logger.info("Resume parsed")

Logs are written to `logs/app.log`.

## Run tests

    pytest

## Code standards

See [docs/CODE_STANDARDS.md](docs/CODE_STANDARDS.md).