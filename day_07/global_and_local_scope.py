import random
from art import logo, heart_full, heart_empty

MAX_LIVES = {'easy': 10, 'hard': 5}


def show_lives(lives, max_lives):
    hearts = heart_full * lives + heart_empty * (max_lives - lives)
    return hearts


def check_guess(guess, secret):
    if guess < secret:
        print("Too low. Guess again!")
        return False
    elif guess > secret:
        print("Too high. Guess again!")
        return False
    else:
        return True


def choose_difficulty():
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if choice in ('easy', 'hard'):
            return choice
        print("Please enter 'easy' or 'hard'.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).lower().strip()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def play_round(difficulty):
    secret = random.randint(1, 100)
    lives = MAX_LIVES[difficulty]
    max_lives = lives

    print(f"\nI'm thinking of a number between 1 and 100. You're playing on {difficulty.upper()} mode.")

    while lives > 0:
        print(f"\nYou have {show_lives(lives, max_lives)} lives remaining.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            continue

        if check_guess(guess, secret):
            print(f"You got it! The answer was {secret}.")
            return True

        lives -= 1
        if lives == 0:
            print(f"You lost! The number was {secret}.")
            return False


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    try:
        difficulty = choose_difficulty()

        while True:
            play_round(difficulty)

            if ask_yes_no("\nDo you want to play again? Type 'yes' or 'no': "):
                if ask_yes_no("Change difficulty? Type 'yes' or 'no': "):
                    difficulty = choose_difficulty()
            else:
                print("Thanks for playing! Goodbye!")
                break

    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")


game()
