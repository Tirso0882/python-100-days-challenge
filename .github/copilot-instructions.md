# Python 100 Days Challenge — Copilot Instructions

## Project Overview
This is a daily Python practice repo. Each day lives in its own `day_X/` folder with one or more `.py` files exploring a Python concept and building a mini-project.

## Repository Structure
- `day_X/` — Each day's code (e.g. `day_1/`, `day_2/`, etc.)
- `README.md` — Daily log table tracking topics and projects
- `.github/skills/ship-day/SKILL.md` — Skill for committing completed days

## Code Standards
- **Python 3.12+** — No external dependencies, standard library only
- Use `snake_case` for variables and functions
- Use `UPPER_CASE` for constants
- Keep code beginner-friendly and readable
- Add `input()` validation for interactive programs (use `while True` loops for re-prompting)
- Use functions to avoid code duplication
- Separate ASCII art and data into their own modules (e.g. `art.py`, `words.py`)

## How to Run
```bash
python day_X/<main_file>.py
```

## Ship Day Workflow
When asked to "ship day X", "commit day X", or "done with day X", follow the skill at `.github/skills/ship-day/SKILL.md` to validate, update README, and commit.

## Key Guidelines
1. Never commit code with errors — always validate first
2. Keep each day's code self-contained in its folder
3. Update the README daily log table when shipping a day
4. Use `git push` only, never `git push --force`
