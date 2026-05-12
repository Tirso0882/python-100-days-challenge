import random
import os
from art import logo, vs, lose_art
from game_data import data


def format_character(character, label):
    """Return a formatted string like 'Compare A: Name, a Description, from Country.'"""
    return f"Compare {label}: {character['name']}, a {character['description']}, from {character['country']}."


def pick_character(data):
    """Pick a random character from data that isn't the same as exclude."""
    return random.choice(data)


def check_answer(guess: str, char_a: int, char_b: int):
    """Return True if the user's guess is correct."""
    if char_a["follower_count"] > char_b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"
    

def clear_console():
    os.system('clear')


def play_game():
    """Run the game loop. Owns the score variable."""
    
    print("Welcome to the Higher Lower Game!")
    print(logo)
    account_1 = pick_character(data=data)
    account_2 = pick_character(data=data)
    score = 0
    while True:
        print(format_character(character=account_1, label="A"))
        print(vs)
        print(format_character(character=account_2, label="B"))

        guess: str = input("Who has more followers? Type 'A' or 'B' to choose: ").lower().strip()

        right_answer = check_answer(guess=guess, char_a=account_1, char_b=account_2)
        
        if right_answer == True:
            score += 1
            
            print(logo)
            print(f"You're right! Current score: {score}")
        
            account_1 = pick_character(data=data)
            account_2 = pick_character(data=data)
        else:
            clear_console()

            print(f"You lose:(.\nFinal score: {score}")
            print(lose_art)
            break


play_game()
