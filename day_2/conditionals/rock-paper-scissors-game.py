import random
import time
import rps_art

BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

BEATS = {0: 2, 1: 0, 2: 1}  # rock beats scissors, paper beats rock, scissors beats paper


def get_choice(prompt: str) -> int:
    while True:
        print(f"{CYAN}{prompt}{RESET}")
        print("  0 = Rock  |  1 = Paper  |  2 = Scissors")
        try:
            choice = int(input("Your choice: ").strip())
            if choice in (0, 1, 2):
                return choice
            print(f"{RED}Please enter 0, 1, or 2.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number (0, 1, or 2).{RESET}")


def get_mode() -> str:
    while True:
        print(f"\n{BOLD}Select mode:{RESET}")
        print("  1 = Player vs Computer")
        print("  2 = Player vs Player")
        choice = input("Enter 1 or 2: ").strip()
        if choice in ("1", "2"):
            return choice
        print(f"{RED}Please enter 1 or 2.{RESET}")


def resolve(c1: int, c2: int) -> str:
    if c1 == c2:
        return "tie"
    if BEATS[c1] == c2:
        return "p1"
    return "p2"


def show_round(name1: str, c1: int, name2: str, c2: int, result: str):
    print(f"\n{BOLD}{'─' * 44}{RESET}")
    print(f"  {BOLD}{name1}{RESET} chose:{rps_art.choices_art[c1]}", end="")
    print(f"  {BOLD}{name2}{RESET} chose:{rps_art.choices_art[c2]}", end="")
    print(f"  {BOLD}{rps_art.choices_name[c1]}{RESET}  vs  {BOLD}{rps_art.choices_name[c2]}{RESET}")
    print()
    if result == "tie":
        print(f"{YELLOW}  It's a tie!{RESET}")
    elif result == "p1":
        print(f"{GREEN}  {name1} wins this round!{RESET}")
    else:
        print(f"{GREEN}  {name2} wins this round!{RESET}")
    print(f"{BOLD}{'─' * 44}{RESET}")


def show_score(name1: str, s1: int, name2: str, s2: int):
    print(f"\n  {BOLD}Score  |  {name1}: {s1}  —  {name2}: {s2}{RESET}\n")


def countdown():
    print(f"\n{BOLD}", end="", flush=True)
    for word in ["Rock...", "Paper...", "Scissors..."]:
        print(word, end=" ", flush=True)
        time.sleep(0.6)
    print(f"SHOOT!{RESET}\n")
    time.sleep(0.3)


print(rps_art.logo)

mode = get_mode()

p1_name = input(f"\n{CYAN}Enter Player 1 name: {RESET}").strip() or "Player 1"
if mode == "2":
    p2_name = input(f"{CYAN}Enter Player 2 name: {RESET}").strip() or "Player 2"
else:
    p2_name = "Computer"

p1_score = p2_score = 0

while True:
    print(f"\n{MAGENTA}{'═' * 44}{RESET}")
    print(f"  {BOLD}New Round{RESET}  —  {p1_name}: {p1_score}  |  {p2_name}: {p2_score}")
    print(f"{MAGENTA}{'═' * 44}{RESET}")

    p1_choice = get_choice(f"\n{p1_name}, make your choice:")

    if mode == "2":
        input(f"\n{YELLOW}Pass to {p2_name} and press Enter...{RESET}")
        print("\n" * 15)
        p2_choice = get_choice(f"{p2_name}, make your choice:")
    else:
        p2_choice = random.randint(0, 2)

    countdown()

    result = resolve(p1_choice, p2_choice)

    if result == "p1":
        p1_score += 1
    elif result == "p2":
        p2_score += 1

    show_round(p1_name, p1_choice, p2_name, p2_choice, result)
    show_score(p1_name, p1_score, p2_name, p2_score)

    again = input("Play another round? (yes/no): ").strip().lower()
    if again != "yes":
        print(f"\n{BOLD}{'═' * 44}{RESET}")
        print(f"  {BOLD}Final Score{RESET}")
        print(f"  {p1_name}: {p1_score}  |  {p2_name}: {p2_score}")
        if p1_score > p2_score:
            print(f"\n  {GREEN}{BOLD}Overall winner: {p1_name}!{RESET}")
        elif p2_score > p1_score:
            print(f"\n  {GREEN}{BOLD}Overall winner: {p2_name}!{RESET}")
        else:
            print(f"\n  {YELLOW}{BOLD}Overall result: It's a draw!{RESET}")
        print(f"{BOLD}{'═' * 44}{RESET}\n")
        break


    
    
    
