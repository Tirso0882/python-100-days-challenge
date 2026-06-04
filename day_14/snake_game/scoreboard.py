"""ScoreBoard — HUD rendering with score, combo, level, and high score persistence."""

import json
import math
import os

from config import (
    CANVAS_WIDTH, CANVAS_HEIGHT, BG_COLOR,
    INITIAL_SPEED, MIN_SPEED,
)
from utils import lerp_color

HIGH_SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_score.json")


class ScoreBoard:
    """Tracks score, combo, level and renders the in-game HUD."""

    def __init__(self):
        self.score = 0
        self.high_score = self._load_high_score()
        self.combo = 0
        self.combo_timer = 0
        self.level = 1
        self.score_popups = []  # (x, y, text, life, color)

    def reset(self):
        """Reset score state for a new game (keeps high score)."""
        self.score = 0
        self.combo = 0
        self.combo_timer = 0
        self.level = 1
        self.score_popups = []

    def add_score(self, base_points, food_color, fx, fy):
        """Add points with combo multiplier and create popup."""
        self.combo += 1
        self.combo_timer = 30
        points = base_points * max(1, self.combo)
        self.score += points

        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()

        # Create floating score popup
        self.score_popups.append((fx, fy, f"+{points}", 1.0, food_color))
        return points

    def update(self):
        """Tick combo timer and decay popups."""
        if self.combo_timer > 0:
            self.combo_timer -= 1
        else:
            self.combo = 0

        # Decay popups (move up and fade)
        self.score_popups = [
            (x, y - 1, text, life - 0.03, color)
            for x, y, text, life, color in self.score_popups
            if life > 0.03
        ]

    def check_level_up(self, current_speed):
        """Check for level up. Returns new speed if leveled up, else None."""
        new_level = self.score // 10 + 1
        if new_level > self.level:
            self.level = new_level
            new_speed = max(MIN_SPEED, INITIAL_SPEED - (self.level - 1) * 6)
            return new_speed
        return None

    def draw(self, canvas, snake_length, current_speed):
        """Render the full HUD."""
        # Score (top-left)
        canvas.create_text(
            15, 20, anchor="w",
            text=f"SCORE: {self.score}",
            fill="#00ff88", font=("Courier", 16, "bold")
        )

        # High score (top-right)
        canvas.create_text(
            CANVAS_WIDTH - 15, 20, anchor="e",
            text=f"BEST: {self.high_score}",
            fill="#666688", font=("Courier", 14, "bold")
        )

        # Level (top-center)
        canvas.create_text(
            CANVAS_WIDTH // 2, 20, anchor="center",
            text=f"LEVEL {self.level}",
            fill="#4466cc", font=("Courier", 14, "bold")
        )

        # Combo display
        if self.combo > 1:
            combo_color = lerp_color("#ffaa00", "#ff3366", min(1, self.combo / 10))
            combo_size = 16 + min(8, self.combo)
            canvas.create_text(
                CANVAS_WIDTH // 2, 50, anchor="center",
                text=f"COMBO x{self.combo}!",
                fill=combo_color,
                font=("Courier", combo_size, "bold")
            )

        # Speed bar
        speed_pct = int((INITIAL_SPEED - current_speed) / (INITIAL_SPEED - MIN_SPEED) * 100)
        bar_width = 100
        bar_x, bar_y = 15, 45
        canvas.create_rectangle(
            bar_x, bar_y, bar_x + bar_width, bar_y + 6,
            fill="#111128", outline="#333355"
        )
        fill_width = int(bar_width * speed_pct / 100)
        speed_color = lerp_color("#00cc44", "#ff3333", speed_pct / 100)
        canvas.create_rectangle(
            bar_x, bar_y, bar_x + fill_width, bar_y + 6,
            fill=speed_color, outline=""
        )
        canvas.create_text(
            bar_x + bar_width + 8, bar_y + 3, anchor="w",
            text="SPD", fill="#555577", font=("Courier", 8)
        )

        # Snake length
        canvas.create_text(
            15, 65, anchor="w",
            text=f"LENGTH: {snake_length}",
            fill="#448866", font=("Courier", 11)
        )

    def draw_popups(self, canvas, offset_x=0, offset_y=0):
        """Render floating score popups."""
        for x, y, text, life, color in self.score_popups:
            popup_color = lerp_color(BG_COLOR, color, life)
            font_size = int(14 + (1 - life) * 4)
            canvas.create_text(
                x + offset_x, y + offset_y - 10,
                text=text, fill=popup_color,
                font=("Courier", font_size, "bold")
            )

    def draw_game_over(self, canvas, snake_length, frame_count, death_reason=""):
        """Render the game over overlay."""
        canvas.create_rectangle(
            0, 0, CANVAS_WIDTH, CANVAS_HEIGHT,
            fill="#000000", stipple="gray50"
        )

        canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 3,
            text="GAME OVER",
            fill="#ff3366", font=("Courier", 44, "bold")
        )

        # Show death reason
        if death_reason:
            canvas.create_text(
                CANVAS_WIDTH // 2, CANVAS_HEIGHT // 3 + 45,
                text=death_reason,
                fill="#ff8844", font=("Courier", 20)
            )

        stats = [
            f"Final Score: {self.score}",
            f"Snake Length: {snake_length}",
            f"Level Reached: {self.level}",
            f"High Score: {self.high_score}",
        ]
        for i, stat in enumerate(stats):
            color = "#ffaa00" if "High Score" in stat and self.score >= self.high_score else "#aaaacc"
            canvas.create_text(
                CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + i * 35,
                text=stat, fill=color, font=("Courier", 18)
            )

        if self.score >= self.high_score and self.score > 0:
            pulse = math.sin(frame_count * 0.1) * 0.3 + 0.7
            canvas.create_text(
                CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 40,
                text="NEW HIGH SCORE!",
                fill=lerp_color("#ffaa00", "#ff3366", pulse),
                font=("Courier", 20, "bold")
            )

        blink = ">" if int(frame_count * 0.05) % 2 == 0 else " "
        canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT * 3 // 4,
            text=f"{blink} Press R to Restart {blink}",
            fill="#aaaacc", font=("Courier", 16, "bold")
        )

    def _load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                data = json.load(f)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def _save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as f:
            json.dump({"high_score": self.high_score}, f)
        