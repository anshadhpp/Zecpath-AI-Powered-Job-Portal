# Code Standards & Documentation Format

## Style
- Follow PEP 8; format with black, lint with ruff.
- Add type hints to all public functions.
- Use snake_case for functions and variables, PascalCase for classes, UPPER_CASE for constants.
- Use `utils.logger.get_logger(__name__)` instead of `print()`.
- Never commit secrets; keep them in `.env`.

## Documentation format
- Every module starts with a one-line docstring naming the PRD phase it implements.
- Public functions use Google-style docstrings (Args, Returns).

## Git workflow
- Branches: `main` (stable), `dev` (integration), `feature/<name>`.
- Commit messages: `feat(ats): add keyword matcher`, `fix(parser): handle empty PDF`, `docs:`, `test:`.
- Run `git pull` before starting work and before pushing.

## Testing
- Every new function needs a test in `tests/`.
- Test files are named `test_<module>.py`.
- Use only sample data in `data/samples/`; never commit real candidate data.

## Logging
- Levels: DEBUG for internals, INFO for milestones, WARNING for recoverable issues, ERROR for failures.
- Logs are written to `logs/app.log` and are never committed to Git.
