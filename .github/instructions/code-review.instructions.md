---
applyTo: "**/*.py"
description: "Auto-applies Python code review nudges when editing .py files. Checks PEP8, idiomatic patterns, and common beginner mistakes."
---

When reviewing or editing Python files, briefly note any of the following issues you spot:

## Style
- Variable/function names not in `snake_case`
- Lines exceeding 79 characters
- Missing blank lines between functions/classes (2 above top-level, 1 between methods)
- Inconsistent string quoting within a file

## Idiomatic Python
- Using `range(len(x))` instead of `enumerate(x)`
- Manual index tracking instead of unpacking
- `if x == True` / `if x == None` instead of `if x` / `if x is None`
- String concatenation in loops instead of `"".join()` or f-strings
- Mutable default arguments (`def f(lst=[])`)

## Logic & Safety
- Bare `except:` without specific exception type
- Using `input()` without validation for numeric input
- Unreachable code after `return`/`break`
- Shadowing built-in names (`list`, `dict`, `input`, `id`, `type`)

## Keep It Light
- Only flag issues in code being actively edited
- Suggest the fix inline, don't lecture
- If the code is clean, say nothing — silence means approval
