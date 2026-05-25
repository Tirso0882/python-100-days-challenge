import random

BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+']


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value >= 0:
                return value
            print(f"{RED}Please enter 0 or a positive number.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid whole number.{RESET}")


def strength_label(total: int, nr_symbols: int, nr_numbers: int) -> str:
    if total >= 16 and nr_symbols >= 2 and nr_numbers >= 2:
        return f"{GREEN}Very Strong 💪{RESET}"
    if total >= 12 and nr_symbols >= 1 and nr_numbers >= 1:
        return f"{GREEN}Strong{RESET}"
    if total >= 8:
        return f"{YELLOW}Moderate{RESET}"
    return f"{RED}Weak{RESET}"


def generate_password(nr_letters: int, nr_numbers: int, nr_symbols: int) -> str:
    # --- For loops: build each character group separately ---
    password_chars = []

    for _ in range(nr_letters):
        password_chars.append(random.choice(LETTERS))

    for _ in range(nr_numbers):
        password_chars.append(random.choice(NUMBERS))

    for _ in range(nr_symbols):
        password_chars.append(random.choice(SYMBOLS))

    # Shuffle so letters/numbers/symbols aren't always in the same order
    random.shuffle(password_chars)

    # --- For loop: assemble the final string character by character ---
    pwd = ""
    for char in password_chars:
        pwd += char

    return pwd


print(f"""
{BOLD}{MAGENTA}╔══════════════════════════════╗
║    🔐 Password Generator     ║
╚══════════════════════════════╝{RESET}
""")

history = []

while True:
    print(f"{CYAN}Configure your password:{RESET}")
    nr_letters = get_positive_int("  How many letters?  ")
    nr_numbers = get_positive_int("  How many numbers?  ")
    nr_symbols = get_positive_int("  How many symbols?  ")

    total = nr_letters + nr_numbers + nr_symbols
    if total == 0:
        print(f"{RED}Password length is 0 — please enter at least one character.{RESET}\n")
        continue

    password = generate_password(nr_letters, nr_numbers, nr_symbols)
    history.append(password)

    strength = strength_label(total, nr_symbols, nr_numbers)

    print(f"""
{BOLD}{'─' * 34}{RESET}
  Password : {BOLD}{GREEN}{password}{RESET}
  Length   : {total} characters
  Strength : {strength}
  Breakdown: {nr_letters} letters · {nr_numbers} numbers · {nr_symbols} symbols
{BOLD}{'─' * 34}{RESET}""")

    print(f"\n{CYAN}What would you like to do?{RESET}")
    print("  1 = Generate another password")
    print("  2 = Show password history")
    print("  3 = Quit")

    while True:
        action = input("Choice: ").strip()
        if action in ("1", "2", "3"):
            break
        print(f"{RED}Please enter 1, 2, or 3.{RESET}")

    if action == "2":
        print(f"\n{BOLD}Password history ({len(history)} generated):{RESET}")
        for i, pwd in enumerate(history, start=1):
            print(f"  {i}. {pwd}")
        print()
        input("Press Enter to continue...\n")
    elif action == "3":
        print(f"\n{GREEN}{BOLD}Your last password: {history[-1]}{RESET}")
        print("Stay safe! 👋\n")
        break
