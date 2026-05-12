import random
from art import logo, vs, lose_art
from game_data import data

# Build game using the Decomposition method
# 1. Understand the Problem First (Input → Output)
# Before writing code, answer:

# What are the inputs? (user input, data, files)
# What is the output? (display, return value)
# What are the rules/constraints?

# Example -> Input: user picks A or B → Output: tell them if correct, track score → Rules: keep going until wrong, pick new characters each round

# 2. Break Into Functions by Responsibility
# Each function should do one thing. Ask: "What are the distinct actions?"

# For this game, the actions are:

# Format and display a character
# Pick two random characters (ensure they're different)
# Check the answer
# Run the game loop

# Step 1: Pseudocode: Write the steps in plain English
# 1. Welcome message
print("Welcome to the Higher Lower Game!")

# 2. Pick 2 different random accounts from the game data.
random_account_1 = random.choice(data)
random_account_2 = random.choice(data)

# 3. Displpay the 2 accounts to the user in a nice format.
print(logo)
print(f"Compare A: {random_account_1['name']}, a {random_account_1['description']}, from {random_account_1['country']}.")
print(vs)
print(f"Against B: {random_account_2['name']}, a {random_account_2['description']}, from {random_account_2['country']}.")

#  4. Ask user to pick A or B
question: str = input("Who has more followers? Type 'A' or 'B' to choose: ").lower().strip()

# 5 Check if answer is correct
# - If yes: increase score, pick new character, repeat from step 3
# - If no: show final score, end game
score = 0

if question == 'a':
    if random_account_1["follower_count"] > random_account_2["follower_count"]:
        print("You're right!")
        score += 1
        print(f"Current score: {score}")
    else:
        print(lose_art)
        print(f"Sorry, that's wrong.\nFinal score: {score}")

# Step 3: Build It - One Function at a Time
# Start with a clean file. Try writing each function yourself based on these signatures -> higher_lower_game.py




