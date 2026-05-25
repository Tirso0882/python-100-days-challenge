import bid_art
import time

BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"


def clear_screen():
    print("\n" * 20)


def get_name(existing: dict) -> str:
    while True:
        name = input(f"{CYAN}What's your name? {RESET}").strip()
        if not name:
            print(f"{RED}Name cannot be empty. Try again.{RESET}")
        elif name.lower() in (k.lower() for k in existing):
            print(f"{YELLOW}'{name}' has already placed a bid. Bidder names must be unique.{RESET}")
        else:
            return name


def get_bid() -> float:
    while True:
        try:
            bid = float(input(f"{CYAN}What's your bid? ${RESET}").strip())
            if bid <= 0:
                print(f"{RED}Bid must be a positive amount. Try again.{RESET}")
            else:
                return bid
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")


def find_winner(results: dict) -> tuple[str, float]:
    return max(results.items(), key=lambda item: item[1])


def reveal_winner(name: str, bid: float, total: int):
    print(f"\n{BOLD}{'=' * 40}{RESET}")
    print(f"{BOLD}  Auction closed! {total} bidder(s) participated.{RESET}")
    print(f"{BOLD}{'=' * 40}{RESET}")
    print(f"\n  Calculating winner", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(0.4)
    print(f"{BOLD}{GREEN}  Winner: {name}{RESET}")
    print(f"{BOLD}{GREEN}  Winning bid: ${bid:,.2f}{RESET}")
    print(f"\n{BOLD}{'=' * 40}{RESET}\n")


print(bid_art.logo)
print(f"{BOLD}Welcome to the Secret Auction!{RESET}\n")

results = {}

while True:
    name = get_name(results)
    bid = get_bid()
    results[name] = bid
    print(f"{GREEN}Bid recorded for {name}!{RESET}")

    while True:
        more = input("\nAre there any other bidders? (yes/no): ").strip().lower()
        if more in ("yes", "no"):
            break
        print(f"{RED}Please type 'yes' or 'no'.{RESET}")

    if more == "no":
        winner_name, max_bid = find_winner(results)
        reveal_winner(winner_name, max_bid, len(results))
        break

    clear_screen()
    print(bid_art.logo)
    print(f"{BOLD}Next bidder — screen cleared for privacy.{RESET}\n")




