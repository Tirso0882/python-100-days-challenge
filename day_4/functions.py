# ========================================================================================================================
# the Argument is the value of the parameter that we pass in the function when we call it. In this case, the parameter is name and the argument is "Angela".
# def greet_with_name(name: str) -> str:
#   print(f"Hello {name}")
#   print("How do you do?")
#   print("Nice to meet you")
#   print("Isn't the weather nice today?")

# greet_with_name(name="Angela")


# def greet_with(name: str, location: str) -> str:
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with(name="Angela", location="London")


# ========================================================================================================================
# def calculate_love_score(name1: str, name2: str) -> str:
#     concatenate_names = str(name1 + name2).lower()
#     true_score = concatenate_names.count("t") + concatenate_names.count("r") + concatenate_names.count("u") + concatenate_names.count("e")
#     love_score = concatenate_names.count("l") + concatenate_names.count("o") + concatenate_names.count("v") + concatenate_names.count("e")
#     total_score = int(str(true_score) + str(love_score))
#     if total_score < 10 or total_score > 90:
#         return f"Your love score is {total_score}, you go together like coke and mentos."
#     elif total_score >= 40 and total_score <= 50:
#         return f"Your love score is {total_score}, you are alright together."
#     else:
#         return f"Your love score is {total_score}."
    
# print(calculate_love_score("Kanye West", "Kim Kardashian"))


# ========================================================================================================================
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar_cipher(message: str, shift: int, direction: str) -> str:
    """Encrypt or decrypt a message using the Caesar cipher.

    Non-alphabet characters (spaces, punctuation, digits) are preserved as-is.
    The shift is normalised with modulo so any integer works (including negatives).
    """
    result = ""
    # Reverse shift for decryption
    effective_shift = shift if direction == "encode" else -shift

    for char in message.lower():
        if char in ALPHABET:
            new_index = (ALPHABET.index(char) + effective_shift) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            # Preserve spaces, punctuation, digits unchanged
            result += char

    return result


def get_shift() -> int:
    while True:
        try:
            shift = int(input(f"{CYAN}  Shift number: {RESET}").strip())
            return shift % len(ALPHABET)   # normalise to 0-25
        except ValueError:
            print(f"{RED}  Please enter a whole number.{RESET}")


def get_direction() -> str:
    while True:
        choice = input(f"{CYAN}  Type 'encode' or 'decode': {RESET}").strip().lower()
        if choice in ("encode", "decode"):
            return choice
        print(f"{RED}  Please type exactly 'encode' or 'decode'.{RESET}")


print(f"""
{BOLD}{MAGENTA}╔══════════════════════════════════╗
║   🔐 Caesar Cipher Machine       ║
╚══════════════════════════════════╝{RESET}
Encode or decode messages using a
letter-shift (Caesar cipher).
""")

history = []

while True:
    direction = get_direction()
    text = input(f"{CYAN}  Your message: {RESET}").strip()

    if not text:
        print(f"{RED}  Message cannot be empty.{RESET}\n")
        continue

    shift = get_shift()
    output = caesar_cipher(message=text, shift=shift, direction=direction)

    action_label = "Encoded" if direction == "encode" else "Decoded"
    history.append((direction, text, shift, output))

    print(f"""
{BOLD}{'─' * 38}{RESET}
  {action_label} message : {BOLD}{GREEN}{output}{RESET}
  Original        : {text}
  Shift applied   : {shift}
{BOLD}{'─' * 38}{RESET}""")

    print(f"\n{CYAN}What next?{RESET}")
    print("  1 = Encode / decode another message")
    print("  2 = Show history")
    print("  3 = Quit")

    while True:
        action = input("Choice: ").strip()
        if action in ("1", "2", "3"):
            break
        print(f"{RED}  Please enter 1, 2, or 3.{RESET}")

    if action == "2":
        print(f"\n{BOLD}Session history ({len(history)} operation(s)):{RESET}")
        for i, (d, original, s, result) in enumerate(history, start=1):
            arrow = "→" if d == "encode" else "←"
            print(f"  {i}. [{d.upper()}] shift={s}  {original!r} {arrow} {result!r}")
        print()
        input("Press Enter to continue...\n")
    elif action == "3":
        print(f"\n{GREEN}{BOLD}Goodbye! 👋{RESET}\n")
        break
    else:
        print()


# ========================================================================================================================