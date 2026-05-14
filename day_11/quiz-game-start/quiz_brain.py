import random
from art import (
    CORRECT_ART, WRONG_ART, GAME_OVER_ART, PERFECT_SCORE_ART,
    STREAK_MESSAGES, TAUNT_MESSAGES,
    CYAN, YELLOW, GREEN, RED, MAGENTA, BOLD, RESET, WHITE
)


class QuizBrain:
    def __init__(self, q_list: list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        self.streak = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        total = len(self.question_list)

        # Progress bar
        progress = int((self.question_number / total) * 20)
        bar = f"{GREEN}{'█' * progress}{WHITE}{'░' * (20 - progress)}{RESET}"
        print(f"\n  [{bar}] {self.question_number}/{total}")
        print(f"  {CYAN}{'─' * 50}{RESET}")

        # Random taunt for fun
        taunt = random.choice(TAUNT_MESSAGES)
        print(f"  {taunt}\n")

        print(f"  {YELLOW}{BOLD}Q.{self.question_number}:{RESET} {WHITE}{current_question.text}{RESET}")
        print(f"  {CYAN}{'─' * 50}{RESET}")

        user_answer = self._get_valid_answer()
        correct_answer = current_question.answer
        self._check_answer(user_answer, correct_answer)

    def _get_valid_answer(self):
        while True:
            answer = input(f"\n  {MAGENTA}👉 True or False?: {RESET}").strip().lower()
            if answer in ("true", "false", "t", "f"):
                if answer in ("t", "true"):
                    return "True"
                return "False"
            print(f"  {RED}⚠️  Please enter 'True' or 'False' (or T/F){RESET}")

    def _check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.streak += 1
            print(CORRECT_ART)
            if self.streak >= 2:
                idx = min(self.streak - 2, len(STREAK_MESSAGES) - 1)
                print(f"  {STREAK_MESSAGES[idx]}")
        else:
            self.streak = 0
            print(WRONG_ART)
            print(f"  {WHITE}The correct answer was: {GREEN}{BOLD}{correct_answer}{RESET}")

        print(f"\n  {CYAN}📊 Score: {YELLOW}{BOLD}{self.score}/{self.question_number}{RESET}")

    def show_final_score(self):
        print(GAME_OVER_ART)
        total = len(self.question_list)
        percentage = int((self.score / total) * 100)

        if self.score == total:
            print(PERFECT_SCORE_ART)
        elif percentage >= 80:
            print(f"  {GREEN}{BOLD}🎊 Amazing! You're a trivia wizard! 🧙{RESET}")
        elif percentage >= 50:
            print(f"  {YELLOW}{BOLD}👍 Not bad! You know some stuff! 📚{RESET}")
        else:
            print(f"  {RED}{BOLD}😅 Better luck next time, champ! 💪{RESET}")

        print(f"\n  {WHITE}{'═' * 40}")
        print(f"  {BOLD}  Final Score: {YELLOW}{self.score}/{total} ({percentage}%){RESET}")
        print(f"  {WHITE}{'═' * 40}{RESET}\n")
