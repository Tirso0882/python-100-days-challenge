import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import LOGO, CYAN, YELLOW, MAGENTA, BOLD, RESET, WHITE, GREEN


def get_player_name():
    while True:
        name = input(f"  {YELLOW}👤 Enter your name, brave quizzer: {RESET}").strip()
        if name:
            return name
        print(f"  {MAGENTA}Come on, even 'Bob' works! Try again.{RESET}")


def get_question_count(max_questions):
    print(f"\n  {CYAN}We have {WHITE}{BOLD}{max_questions}{RESET}{CYAN} mind-bending questions loaded!{RESET}")
    while True:
        choice = input(f"  {YELLOW}🎯 How many do you want to attempt? (1-{max_questions}, or 'all'): {RESET}").strip().lower()
        if choice == "all":
            return max_questions
        try:
            count = int(choice)
            if 1 <= count <= max_questions:
                return count
            print(f"  {MAGENTA}Pick a number between 1 and {max_questions}!{RESET}")
        except ValueError:
            print(f"  {MAGENTA}That's not a number... or 'all'. Try again!{RESET}")


def play_again():
    while True:
        choice = input(f"\n  {YELLOW}🔄 Play again? (yes/no): {RESET}").strip().lower()
        if choice in ("yes", "y"):
            return True
        if choice in ("no", "n"):
            return False
        print(f"  {MAGENTA}Just say yes or no! 🙃{RESET}")


def main():
    print(LOGO)
    print(f"  {WHITE}{BOLD}Welcome to the Ultimate True/False Quiz!{RESET}")
    print(f"  {CYAN}Test your knowledge with wild, weird, and wonderful facts.{RESET}\n")

    player_name = get_player_name()
    print(f"\n  {GREEN}{BOLD}Let's go, {player_name}! 🚀{RESET}\n")

    while True:
        # Shuffle questions each round
        shuffled_data = random.sample(question_data, len(question_data))
        num_questions = get_question_count(len(shuffled_data))

        selected_data = shuffled_data[:num_questions]
        question_bank = []
        for question in selected_data:
            new_question = Question(q_text=question["text"], q_answer=question["answer"])
            question_bank.append(new_question)

        quiz = QuizBrain(question_bank)

        print(f"\n  {CYAN}{'═' * 50}")
        print(f"  {BOLD}  🧠 {num_questions} questions coming your way, {player_name}!{RESET}")
        print(f"  {CYAN}{'═' * 50}{RESET}")

        while quiz.still_has_question():
            quiz.next_question()

        quiz.show_final_score()

        if not play_again():
            print(f"\n  {YELLOW}{BOLD}👋 Thanks for playing, {player_name}! See you next time! 🌟{RESET}\n")
            break
        print(f"\n  {GREEN}{BOLD}🎮 Round 2... FIGHT! 🥊{RESET}")


if __name__ == "__main__":
    main()

