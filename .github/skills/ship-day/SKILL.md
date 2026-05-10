# Ship Day Skill

Ship a completed day of the Python 100 Days Challenge — validate, document, commit, and push.

## Trigger Phrases

- "ship day X"
- "commit day X"
- "done with day X"
- "push day X"
- "I'm done with day X, ship it"

Where X is the day number (e.g. 7).

---

## Workflow

### Step 1: Identify the Day

- Extract the day number from the user's message.
- Confirm the folder `day_X/` exists in the workspace root.
- If it doesn't exist, stop and tell the user.

### Step 2: Check for Errors

- Run `get_errors` on all files inside `day_X/`.
- Run each Python file in the folder to check for runtime errors: `python day_X/<file>.py` (use a short timeout, provide test input if interactive).
- If there are errors, report them and **stop** — do not commit broken code.

### Step 3: Read the Code and Summarize

- Read all `.py` files in `day_X/`.
- Identify:
  - **Topic**: The main Python concept practiced (e.g. "Functions", "Dictionaries & while loops").
  - **Project**: A short emoji + name describing what was built (e.g. "🎯 Number Guessing Game").
  - **Run command**: The main entry point file to run the project (e.g. `python day_7/global_and_local_scope.py`).

### Step 4: Update README.md

- Open `README.md` in the workspace root.
- Find the **Daily Log** table:
  ```
  | Day | Topic | Project |
  |-----|-------|---------|
  ```
- Append a new row at the end of the table:
  ```
  | Day X | <Topic> | <Emoji> <Project Name> |
  ```
- Find the **How to Run** code block and append the run command if not already present:
  ```
  python day_X/<main_file>.py
  ```
- Do NOT modify any other part of the README.

### Step 5: Git Commit and Push

- Stage only the relevant files:
  ```bash
  git add day_X/ README.md
  ```
- Commit with a consistent message format:
  ```bash
  git commit -m "Day X: <Topic> - <Project Name>"
  ```
- Push to the current branch:
  ```bash
  git push
  ```

### Step 6: Confirm

- Tell the user what was committed and pushed.
- Show the README table row that was added.

---

## Rules

- **Never skip Step 2.** Do not commit code with errors.
- **Never force push.** Use `git push` only, never `git push --force`.
- **Ask before pushing** if there are uncommitted changes in other files (outside `day_X/` and `README.md`).
- **Preserve README structure.** Only add to the table and run block — don't reformat or rewrite existing content.
- **One day at a time.** Only process the single day the user specifies.
