# ============================================================
# Day 8 — Debugging Best Practices Guide
# ============================================================
# Debugging is the art of finding and fixing errors in code.
# This guide covers practical techniques with examples.
# ============================================================


# ————————————————————————————————————————————
# 1. DESCRIBE THE PROBLEM
# ————————————————————————————————————————————
# Before touching code, describe what SHOULD happen vs what
# ACTUALLY happens. This narrows the search area.

# Example: "The function should print numbers 1-20, but it
# stops at 19 and never prints the message."

def describe_the_problem():
    """Bug: range stops before end, so 20 is never reached."""

    # BUGGY VERSION
    # for i in range(1, 20):   # range(1,20) goes up to 19!
    #     if i == 20:
    #         print("You got it!")

    # FIXED VERSION — include 20 in the range
    for i in range(1, 21):
        if i == 20:
            print("You got it!")

describe_the_problem()


# ————————————————————————————————————————————
# 2. REPRODUCE THE BUG
# ————————————————————————————————————————————
# Run the code multiple times or with different inputs until
# you can consistently trigger the error.

def reproduce_the_bug():
    """Bug: index sometimes goes out of range because
    randint is inclusive on both ends."""
    from random import randint

    dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]

    # BUGGY VERSION — randint(1, 6) can return 6, but index 6
    # doesn't exist (valid indices are 0-5)
    # dice_num = randint(1, 6)

    # FIXED VERSION — use 0 to 5 for valid indices
    dice_num = randint(0, 5)
    print(dice_images[dice_num])

reproduce_the_bug()


# ————————————————————————————————————————————
# 3. USE PRINT STATEMENTS TO TRACE VALUES
# ————————————————————————————————————————————
# Sprinkle print() calls to see variable values at each step.
# This is the simplest and most universal technique.

def trace_with_print():
    """Bug: wrong total because of an off-by-one in the loop."""
    word = "python"
    letter_count = {}

    for letter in word:
        # Print to see what's happening at each iteration
        print(f"Processing letter: '{letter}'")

        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

        print(f"  Current counts: {letter_count}")

    print(f"Final result: {letter_count}")

trace_with_print()


# ————————————————————————————————————————————
# 4. USE TYPE CHECKING
# ————————————————————————————————————————————
# Many bugs come from unexpected types. Use type() and
# isinstance() to verify data types.

def type_checking_example():
    """Bug: string concatenation instead of addition."""
    user_input = "5"  # Simulating input() which returns a string

    # BUGGY — "5" + "5" = "55", not 10
    # result = user_input + user_input

    # Debug: check the type
    print(f"Type of user_input: {type(user_input)}")

    # FIXED — convert to int first
    result = int(user_input) + int(user_input)
    print(f"Result: {result}")  # 10

type_checking_example()


# ————————————————————————————————————————————
# 5. CHECK BOUNDARY CONDITIONS
# ————————————————————————————————————————————
# Test with edge cases: empty lists, zero, negative numbers,
# first/last elements, very large values.

def boundary_conditions():
    """Bug: function crashes on empty list."""
    def find_max(numbers):
        if not numbers:
            print("List is empty, no max value.")
            return None

        max_value = numbers[0]
        for num in numbers:
            if num > max_value:
                max_value = num
        return max_value

    # Test with normal case
    print(f"Max of [3,1,4,1,5]: {find_max([3, 1, 4, 1, 5])}")
    # Test edge cases
    print(f"Max of []:           {find_max([])}")
    print(f"Max of [42]:         {find_max([42])}")
    print(f"Max of [-1,-5,-2]:   {find_max([-1, -5, -2])}")

boundary_conditions()


# ————————————————————————————————————————————
# 6. USE TRY/EXCEPT TO CATCH ERRORS GRACEFULLY
# ————————————————————————————————————————————
# Wrap risky code in try/except to understand what error
# occurs and where.

def try_except_example():
    """Catch and display the exact error for debugging."""
    test_inputs = ["10", "abc", "0", "5"]

    for value in test_inputs:
        try:
            number = int(value)
            result = 100 / number
            print(f"100 / {value} = {result}")
        except ValueError:
            print(f"ERROR: '{value}' is not a valid number")
        except ZeroDivisionError:
            print(f"ERROR: Cannot divide by zero (input was '{value}')")

try_except_example()


# ————————————————————————————————————————————
# 7. COMMENT OUT SECTIONS / DIVIDE AND CONQUER
# ————————————————————————————————————————————
# Comment out blocks of code to isolate which section
# contains the bug. Then narrow down line by line.

def divide_and_conquer():
    """Isolate the buggy section by commenting out parts."""
    data = [10, 20, 30, 40, 50]

    # Step 1: Does the data look right?
    print(f"Step 1 — data: {data}")  # ✅ OK

    # Step 2: Process data
    doubled = [x * 2 for x in data]
    print(f"Step 2 — doubled: {doubled}")  # ✅ OK

    # Step 3: Filter (this was the buggy line)
    # BUGGY:  filtered = [x for x in doubled if x > 100]
    # FIXED:  use >= instead of > to include 100
    filtered = [x for x in doubled if x >= 60]
    print(f"Step 3 — filtered: {filtered}")

    # Step 4: Sum
    total = sum(filtered)
    print(f"Step 4 — total: {total}")

divide_and_conquer()


# ————————————————————————————————————————————
# 8. USE PYTHON'S BUILT-IN DEBUGGER (pdb)
# ————————————————————————————————————————————
# Add `breakpoint()` to pause execution and inspect
# variables interactively in the terminal.
# Commands: n (next), s (step into), c (continue),
#           p variable (print), q (quit)

def debugger_example():
    """Uncomment the breakpoint() line to try pdb."""
    numbers = [1, 2, 3, 4, 5]
    total = 0

    for num in numbers:
        total += num
        # Uncomment the next line to activate the debugger:
        # breakpoint()

    print(f"Total: {total}")

debugger_example()


# ————————————————————————————————————————————
# 9. USE ASSERT STATEMENTS
# ————————————————————————————————————————————
# Assert lets you verify assumptions. If the condition is
# False, Python raises an AssertionError immediately.

def assert_example():
    """Use assert to catch logic errors early."""
    def calculate_discount(price, discount_pct):
        assert 0 <= discount_pct <= 100, (
            f"Discount must be 0-100, got {discount_pct}"
        )
        return price * (1 - discount_pct / 100)

    print(f"$100 at 20% off: ${calculate_discount(100, 20)}")
    print(f"$50 at 0% off:   ${calculate_discount(50, 0)}")

    # Uncomment to see the AssertionError:
    # print(calculate_discount(100, 150))

assert_example()


# ————————————————————————————————————————————
# 10. READ THE ERROR MESSAGE CAREFULLY
# ————————————————————————————————————————————
# Python error messages (tracebacks) tell you exactly:
#   - The file and line number
#   - The type of error (TypeError, ValueError, etc.)
#   - A description of what went wrong
#
# Common errors and what they mean:
#
#   SyntaxError        → Typo or missing colon/bracket
#   IndentationError   → Wrong spacing/tabs
#   NameError          → Variable not defined or misspelled
#   TypeError          → Wrong type (e.g., "5" + 5)
#   IndexError         → List index out of range
#   KeyError           → Dictionary key doesn't exist
#   ValueError         → Right type, wrong value (e.g., int("abc"))
#   AttributeError     → Object doesn't have that method/property
#   ZeroDivisionError  → Dividing by zero

def read_error_messages():
    """Intentional errors to practice reading tracebacks."""

    # Example: KeyError
    person = {"name": "Alice", "age": 30}

    # BUGGY — "Name" ≠ "name" (case-sensitive!)
    # print(person["Name"])

    # FIXED — use the exact key
    print(person["name"])

    # Safer approach: use .get() with a default
    print(person.get("phone", "No phone on file"))

read_error_messages()


# ============================================================
# DEBUGGING CHECKLIST (use this every time!)
# ============================================================
# 1. Read the error message — what type? what line?
# 2. Describe what should happen vs what actually happens
# 3. Reproduce the bug consistently
# 4. Add print() statements to trace variable values
# 5. Check types with type() or isinstance()
# 6. Test edge cases (empty, zero, negative, boundaries)
# 7. Comment out code to isolate the problem section
# 8. Use try/except to catch and display errors
# 9. Use assert to verify your assumptions
# 10. Use breakpoint() / pdb for interactive debugging
# ============================================================
