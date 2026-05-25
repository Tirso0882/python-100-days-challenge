import random
import os
import time
from art import (
    logo, vs, win_art, streak_art, trophy_art, crown_art,
    scoreboard_art, turn_banner,
    BOLD, RESET, RED, GREEN, YELLOW, CYAN, DIM, PLAYER_COLORS,
)
from game_data import data

MAX_ROUNDS = 10


def clear_console():
    os.system('clear')


def pause(seconds=1.0):
    """Brief dramatic pause."""
    time.sleep(seconds)


def format_character(character, label):
    """Return a formatted string like 'Compare A: Name, a Description, from Country.'"""
    color = GREEN if label == "A" else CYAN
    return (
        f"  {color}{BOLD}[{label}]{RESET} "
        f"{BOLD}{character['name']}{RESET}, "
        f"a {character['description']}, from {character['country']}."
    )


def reveal_counts(char_a, char_b):
    """Show the actual follower counts for both characters."""
    print(f"\n  {GREEN}{BOLD}[A]{RESET} {char_a['name']}: "
          f"{YELLOW}{BOLD}{char_a['follower_count']}M{RESET} followers")
    print(f"  {CYAN}{BOLD}[B]{RESET} {char_b['name']}: "
          f"{YELLOW}{BOLD}{char_b['follower_count']}M{RESET} followers")


def pick_two_different(data_list):
    """Pick two different characters from the data."""
    pair = random.sample(data_list, 2)
    return pair[0], pair[1]


def check_answer(guess, char_a, char_b):
    """Return True if the user's guess is correct."""
    if char_a["follower_count"] > char_b["follower_count"]:
        return guess == "a"
    elif char_b["follower_count"] > char_a["follower_count"]:
        return guess == "b"
    else:
        return True  # tie — any answer is correct


def get_valid_guess():
    """Keep asking until the player types A or B."""
    while True:
        guess = input(f"\n  {BOLD}Who has more followers? Type 'A' or 'B': {RESET}").lower().strip()
        if guess in ("a", "b"):
            return guess
        print(f"  {RED}Invalid input! Please type A or B.{RESET}")


def get_player_count():
    """Ask how many players (1–4)."""
    while True:
        try:
            count = int(input(f"  {BOLD}How many players? (1-4): {RESET}").strip())
            if 1 <= count <= 4:
                return count
            print(f"  {RED}Please enter a number between 1 and 4.{RESET}")
        except ValueError:
            print(f"  {RED}Please enter a valid number.{RESET}")


def get_player_names(count):
    """Collect names for each player."""
    names = []
    for i in range(count):
        color = PLAYER_COLORS[i % len(PLAYER_COLORS)]
        while True:
            name = input(f"  {color}Player {i + 1} name: {RESET}").strip()
            if name:
                names.append(name)
                break
            print(f"  {RED}Name cannot be empty.{RESET}")
    return names


def get_round_count():
    """Ask how many rounds to play (5, 10, or 15)."""
    while True:
        try:
            rounds = int(input(f"  {BOLD}How many rounds? (5 / 10 / 15): {RESET}").strip())
            if rounds in (5, 10, 15):
                return rounds
            print(f"  {RED}Please choose 5, 10, or 15.{RESET}")
        except ValueError:
            print(f"  {RED}Please enter a valid number.{RESET}")


def countdown(message="Get ready"):
    """Fun 3-2-1 countdown."""
    print(f"\n  {BOLD}{message}...{RESET}", end="", flush=True)
    for i in range(3, 0, -1):
        print(f" {YELLOW}{BOLD}{i}{RESET}", end="", flush=True)
        pause(0.6)
    print(f" {GREEN}{BOLD}GO!{RESET}\n")
    pause(0.4)


def play_game():
    """Main game loop with multiplayer support."""
    clear_console()
    print(logo)
    print(f"  {BOLD}Welcome to the Higher Lower Game!{RESET}")
    print(f"  {DIM}Guess who has more Instagram followers.{RESET}\n")

    # Setup
    player_count = get_player_count()
    names = get_player_names(player_count)
    total_rounds = get_round_count()

    players = []
    for i, name in enumerate(names):
        players.append({
            'name': name,
            'index': i,
            'score': 0,
            'streak': 0,
            'best_streak': 0,
        })

    countdown()

    # Game loop — rotate through players for `total_rounds` rounds
    current_player_idx = 0
    for round_num in range(1, total_rounds + 1):
        player = players[current_player_idx]
        color = PLAYER_COLORS[player['index'] % len(PLAYER_COLORS)]

        clear_console()
        print(logo)
        print(f"  {DIM}Round {round_num} of {total_rounds}{RESET}")
        print(scoreboard_art(players))

        if player_count > 1:
            print(turn_banner(player['name'], player['index']))
        else:
            print()

        account_a, account_b = pick_two_different(data)

        print(format_character(character=account_a, label="A"))
        print(vs)
        print(format_character(character=account_b, label="B"))

        guess = get_valid_guess()
        correct = check_answer(guess=guess, char_a=account_a, char_b=account_b)

        # Dramatic reveal
        print(f"\n  {DIM}Revealing...{RESET}", end="", flush=True)
        pause(1.0)
        reveal_counts(account_a, account_b)
        pause(0.5)

        if correct:
            player['score'] += 1
            player['streak'] += 1
            if player['streak'] > player['best_streak']:
                player['best_streak'] = player['streak']

            # Streak bonus
            if player['streak'] >= 3:
                bonus = player['streak'] - 2  # 3-streak = +1, 4-streak = +2, etc.
                player['score'] += bonus
                print(streak_art)
                print(f"  {YELLOW}{BOLD}{player['name']} is on a {player['streak']}-streak! +{bonus} bonus point{'s' if bonus > 1 else ''}!{RESET}")
            else:
                print(f"\n  {GREEN}{BOLD}Correct! +1 point for {player['name']}!{RESET}")
        else:
            player['streak'] = 0
            print(f"\n  {RED}{BOLD}Wrong! {player['name']} loses their streak.{RESET}")

        pause(1.5)

        # Next player
        current_player_idx = (current_player_idx + 1) % player_count

    # === FINAL RESULTS ===
    clear_console()
    print(logo)
    print(trophy_art)
    print(f"\n  {BOLD}{YELLOW}FINAL RESULTS{RESET}\n")
    print(scoreboard_art(players))

    # Find the winner(s)
    top_score = max(p['score'] for p in players)
    winners = [p for p in players if p['score'] == top_score]

    if player_count > 1:
        print(crown_art)
        if len(winners) == 1:
            winner = winners[0]
            wcolor = PLAYER_COLORS[winner['index'] % len(PLAYER_COLORS)]
            print(f"  {wcolor}{BOLD}{winner['name']} wins with {winner['score']} points!{RESET}")
        else:
            tied_names = " & ".join(w['name'] for w in winners)
            print(f"  {YELLOW}{BOLD}It's a tie! {tied_names} tied at {top_score} points!{RESET}")
    else:
        if top_score >= total_rounds:
            print(win_art)
            print(f"  {GREEN}{BOLD}Perfect game! You got every single one!{RESET}")
        elif top_score >= total_rounds * 0.7:
            print(f"  {GREEN}{BOLD}Great job, {players[0]['name']}! {top_score} points!{RESET}")
        else:
            print(f"  {YELLOW}{BOLD}You scored {top_score} points. Keep practicing!{RESET}")

    # Show best streaks
    print(f"\n  {DIM}{'─' * 36}{RESET}")
    for p in players:
        color = PLAYER_COLORS[p['index'] % len(PLAYER_COLORS)]
        print(f"  {color}Best streak for {p['name']}: {p['best_streak']}{RESET}")
    print()


def main():
    """Entry point — handles play again loop."""
    while True:
        play_game()
        while True:
            again = input(f"  {BOLD}Play again? (yes/no): {RESET}").lower().strip()
            if again in ("yes", "y"):
                break
            elif again in ("no", "n"):
                print(f"\n  {CYAN}{BOLD}Thanks for playing! See you next time!{RESET}\n")
                return
            print(f"  {RED}Please type yes or no.{RESET}")


main()
