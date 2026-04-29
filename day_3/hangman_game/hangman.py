import random
import os
import day_3.hangman_game.hangman_art as hangman_art
import day_3.hangman_game.hangman_words as hangman_words
from day_3.hangman_game.hangman_art import RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BOLD, DIM, RESET


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_lives(lives, max_lives):
    hearts = hangman_art.heart_full * lives + hangman_art.heart_empty * (max_lives - lives)
    return f"  Lives: {hearts}"


def show_word(display, chosen_word):
    """Show the word with colors: green for found letters, yellow underscores for blanks."""
    result = ""
    for i, ch in enumerate(display):
        if ch == "_":
            result += f" {YELLOW}{BOLD}_{RESET}"
        else:
            result += f" {GREEN}{BOLD}{ch.upper()}{RESET}"
    return result


def show_guessed_letters(guessed):
    """Show which letters have been guessed, colored by result."""
    if not guessed:
        return ""
    letters = " ".join(sorted(guessed))
    return f"  {DIM}Guessed: [ {letters} ]{RESET}"


def get_word_list(difficulty):
    if difficulty == 1:
        return hangman_words.easy_words
    elif difficulty == 2:
        return hangman_words.medium_words
    else:
        return hangman_words.hard_words


def choose_difficulty():
    print(f"\n  {BOLD}{WHITE}Choose your difficulty:{RESET}\n")
    print(f"    {GREEN}{BOLD}1{RESET} - {GREEN}Easy{RESET}    (short words, 8 lives, 2 hints)")
    print(f"    {YELLOW}{BOLD}2{RESET} - {YELLOW}Medium{RESET}  (medium words, 6 lives, 1 hint)")
    print(f"    {RED}{BOLD}3{RESET} - {RED}Hard{RESET}    (long words, 5 lives, no hints)\n")

    while True:
        choice = input(f"  {CYAN}Enter 1, 2, or 3: {RESET}").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print(f"  {RED}Oops! Please type 1, 2, or 3.{RESET}")


def play_game():
    clear_screen()
    print(hangman_art.logo)

    difficulty = choose_difficulty()
    words = get_word_list(difficulty)
    chosen_word = random.choice(words)

    if difficulty == 1:
        max_lives = 8
        hints_left = 2
    elif difficulty == 2:
        max_lives = 6
        hints_left = 1
    else:
        max_lives = 5
        hints_left = 0

    lives = max_lives
    guessed_letters = set()
    correct_letters = set()
    display = ["_"] * len(chosen_word)

    # Show initial state
    clear_screen()
    print(hangman_art.logo)
    difficulty_names = {1: f"{GREEN}Easy{RESET}", 2: f"{YELLOW}Medium{RESET}", 3: f"{RED}Hard{RESET}"}
    print(f"  Difficulty: {difficulty_names[difficulty]}    Word length: {BOLD}{len(chosen_word)} letters{RESET}")
    print(f"{show_lives(lives, max_lives)}")
    print(hangman_art.stages[min(lives, 6)])
    print(f"  {show_word(display, chosen_word)}\n")
    if hints_left > 0:
        print(f"  {MAGENTA}Hints available: {hints_left} (type '?' for a hint){RESET}\n")

    while True:
        guess = input(f"  {CYAN}{BOLD}Guess a letter{RESET}{CYAN} (or '?' for hint): {RESET}").lower().strip()

        # Hint system
        if guess == "?":
            if hints_left <= 0:
                print(f"  {RED}No hints left!{RESET}")
                continue
            # Reveal a random unguessed letter
            unrevealed = [i for i, ch in enumerate(display) if ch == "_"]
            if unrevealed:
                idx = random.choice(unrevealed)
                reveal_letter = chosen_word[idx]
                display[idx] = reveal_letter
                correct_letters.add(reveal_letter)
                # Reveal ALL occurrences of this letter
                for j, ch in enumerate(chosen_word):
                    if ch == reveal_letter:
                        display[j] = ch
                hints_left -= 1
                clear_screen()
                print(hangman_art.logo)
                print(f"\n  {MAGENTA}Hint! The letter '{BOLD}{reveal_letter.upper()}{RESET}{MAGENTA}' has been revealed!{RESET}")
                print(f"  {MAGENTA}Hints remaining: {hints_left}{RESET}")
                print(f"{show_lives(lives, max_lives)}")
                print(hangman_art.stages[min(lives, 6)])
                print(f"  {show_word(display, chosen_word)}\n")
                print(show_guessed_letters(guessed_letters))

                if "_" not in display:
                    print(hangman_art.win_art)
                    print(f"  {GREEN}{BOLD}The word was: {chosen_word.upper()}{RESET}\n")
                    return True
                continue
            continue

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(f"  {RED}Please enter a single letter (a-z).{RESET}")
            continue

        if guess in guessed_letters:
            print(f"  {YELLOW}You already guessed '{guess.upper()}'! Try a different letter.{RESET}")
            continue

        guessed_letters.add(guess)

        # Check the guess
        if guess in chosen_word:
            correct_letters.add(guess)
            for i, ch in enumerate(chosen_word):
                if ch == guess:
                    display[i] = guess

            clear_screen()
            print(hangman_art.logo)

            # Fun encouraging messages
            cheers = [
                "Nice one!", "Great guess!", "You got it!", "Awesome!",
                "Fantastic!", "Way to go!", "Brilliant!", "Super!",
                "Yes! Nailed it!", "Woohoo!", "Keep it up!",
            ]
            print(f"\n  {GREEN}{BOLD}{random.choice(cheers)}{RESET} {GREEN}'{guess.upper()}' is in the word!{RESET}")
        else:
            lives -= 1

            clear_screen()
            print(hangman_art.logo)

            # Sad messages
            misses = [
                "Oh no!", "Not quite!", "Oops!", "Nope!",
                "Hmm, not that one!", "Aw, try again!", "So close!",
            ]
            print(f"\n  {RED}{random.choice(misses)}{RESET} {RED}'{guess.upper()}' is NOT in the word.{RESET}")

        print(f"{show_lives(lives, max_lives)}")
        print(hangman_art.stages[min(lives, 6)])
        print(f"  {show_word(display, chosen_word)}\n")
        print(show_guessed_letters(guessed_letters))
        if hints_left > 0:
            print(f"  {DIM}Hints remaining: {hints_left}{RESET}")
        print()

        # Check win
        if "_" not in display:
            print(hangman_art.win_art)
            print(f"  {GREEN}{BOLD}The word was: {chosen_word.upper()}{RESET}\n")
            return True

        # Check lose
        if lives == 0:
            print(hangman_art.lose_art)
            print(f"  {YELLOW}The word was: {BOLD}{chosen_word.upper()}{RESET}\n")
            return False


def main():
    score_wins = 0
    score_losses = 0

    while True:
        won = play_game()
        if won:
            score_wins += 1
        else:
            score_losses += 1

        print(f"  {CYAN}{BOLD}--- Scoreboard ---{RESET}")
        print(f"  {GREEN}Wins: {score_wins}{RESET}  |  {RED}Losses: {score_losses}{RESET}\n")

        while True:
            again = input(f"  {CYAN}Play again? (y/n): {RESET}").lower().strip()
            if again in ("y", "n"):
                break
            print(f"  {RED}Please type 'y' or 'n'.{RESET}")

        if again == "n":
            print(f"\n  {MAGENTA}{BOLD}Thanks for playing! See you next time!{RESET}\n")
            break


if __name__ == "__main__":
    main()
