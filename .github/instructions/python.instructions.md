---
applyTo: "**/*.py"
---

# Python Code Conventions

## Style
- Use `snake_case` for variables and functions
- Use `UPPER_CASE` for constants
- Keep code beginner-friendly — prefer clarity over cleverness

## Input Validation
- Always validate `input()` in interactive programs
- Use `while True` with `break` for re-prompting on invalid input
- Use `.lower().strip()` on user input before comparisons
- Wrap `int(input(...))` in try/except `ValueError`

## Structure
- Separate ASCII art into `art.py` modules
- Separate word lists / data into their own modules (e.g. `words.py`)
- Use functions to avoid duplicating logic
- Keep each day's code self-contained in its `day_X/` folder

## Scope
- Prefer local variables over global state
- Use function parameters and return values instead of modifying globals
- Constants defined at module level are fine
