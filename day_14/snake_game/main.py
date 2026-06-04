#!/usr/bin/env python3.12
"""
SNEAKY 3D — Enhanced Snake Game
================================
A visually stunning pseudo-3D snake game with particle effects,
power-ups, combo scoring, and smooth animations.

Controls:
    Arrow Keys / WASD — Move snake
    Space — Pause / Resume
    R — Restart after game over
    Enter — Start game from menu

Architecture:
    main.py       — Game class (loop, input, state machine)
    snake.py      — Snake class (movement, collision, rendering)
    food.py       — FoodItem + FoodManager (types, spawning, rendering)
    scoreboard.py — ScoreBoard (HUD, combos, high score persistence)
    effects.py    — ParticleSystem, ScreenShake, Trail
    config.py     — All constants
    utils.py      — Color utility functions
"""

import math
import sys
import tkinter as tk

# Add parent directory for imports when running as script
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))

from config import (
    CANVAS_WIDTH, CANVAS_HEIGHT, GRID_SIZE, COLS, ROWS,
    BG_COLOR, GRID_COLOR, BORDER_COLOR,
    INITIAL_SPEED, FOOD_COLORS,
)
from utils import lerp_color
from snake import Snake, UP, DOWN, LEFT, RIGHT
from food import FoodManager
from scoreboard import ScoreBoard
from effects import ParticleSystem, ScreenShake, Trail


class Game:
    """Main game controller — state machine, input, update loop, rendering."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SNEAKY 3D")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")

        self.canvas = tk.Canvas(
            self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
            bg=BG_COLOR, highlightthickness=0
        )
        self.canvas.pack()

        # Core game objects
        self.snake = Snake()
        self.food_manager = FoodManager()
        self.scoreboard = ScoreBoard()

        # Effects
        self.particles = ParticleSystem()
        self.shake = ScreenShake()
        self.trail = Trail()

        # Game state
        self.state = "menu"  # menu | playing | paused | game_over
        self.speed = INITIAL_SPEED
        self.frame_count = 0
        self.flash_alpha = 0
        self.death_reason = ""

        # Input
        self.root.bind("<KeyPress>", self._on_key)

        # Start
        self._game_loop()

    # ─── Input ───────────────────────────────────────────────────────────────

    def _on_key(self, event):
        key = event.keysym.lower()

        if self.state == "menu":
            if key in ("return", "space"):
                self._start_game()

        elif self.state == "game_over":
            if key == "r":
                self._start_game()

        elif self.state == "playing":
            if key == "space":
                self.state = "paused"
                return
            direction_map = {
                "up": UP, "w": UP,
                "down": DOWN, "s": DOWN,
                "left": LEFT, "a": LEFT,
                "right": RIGHT, "d": RIGHT,
            }
            if key in direction_map:
                self.snake.set_direction(direction_map[key])

        elif self.state == "paused":
            if key == "space":
                self.state = "playing"

    # ─── State transitions ───────────────────────────────────────────────────

    def _start_game(self):
        self.state = "playing"
        self.speed = INITIAL_SPEED
        self.frame_count = 0
        self.flash_alpha = 0
        self.death_reason = ""

        self.snake.reset()
        self.food_manager.reset()
        self.food_manager.spawn("normal", self.snake.positions_set)
        self.scoreboard.reset()

        self.particles = ParticleSystem()
        self.shake = ScreenShake()
        self.trail = Trail()

    def _trigger_game_over(self, reason=""):
        self.state = "game_over"
        self.death_reason = reason
        # Head explosion
        hx = self.snake.head[0] * GRID_SIZE + GRID_SIZE // 2
        hy = self.snake.head[1] * GRID_SIZE + GRID_SIZE // 2
        self.particles.emit_ring(hx, hy, count=30, color="#ff3333", speed=6, life=1.0)
        self.particles.emit(hx, hy, count=40, color="#ffaa00", spread=8, life=1.2)
        self.shake.trigger(15)
        self.flash_alpha = 0.8

    # ─── Game Loop ───────────────────────────────────────────────────────────

    def _game_loop(self):
        if self.state == "playing":
            self._update()

        self._render()

        delay = self.speed if self.state == "playing" else 33
        self.root.after(delay, self._game_loop)

    def _update(self):
        self.frame_count += 1

        # Move snake (handles growth internally)
        new_head = self.snake.move()

        # Wall collision
        if self.snake.check_wall_collision():
            self._trigger_game_over("Hit the wall!")
            return

        # Self collision
        if self.snake.check_self_collision():
            self._trigger_game_over("Ate yourself!")
            return

        # Track trail
        px = new_head[0] * GRID_SIZE + GRID_SIZE // 2
        py = new_head[1] * GRID_SIZE + GRID_SIZE // 2
        self.trail.add(px, py)

        # Food collision
        eaten_food = self.food_manager.check_collision(new_head)
        if eaten_food:
            self._eat_food(eaten_food)

        # Update food timers / expiration
        self.food_manager.update(self.snake.positions_set)

        # Spawn random power-ups periodically
        if self.frame_count % 50 == 0 and len(self.food_manager.items) < 4:
            self.food_manager.spawn_random_powerup(self.snake.positions_set)

        # Level up check
        new_speed = self.scoreboard.check_level_up(self.speed)
        if new_speed is not None:
            self.speed = new_speed
            self.flash_alpha = 0.15
            self.shake.trigger(2)

        # Update effects
        self.scoreboard.update()
        self.particles.update(0.05)
        self.shake.update()

        if self.flash_alpha > 0:
            self.flash_alpha *= 0.3  # Fast decay so screen stays visible

    def _eat_food(self, food):
        """Handle eating a food item — growth, scoring, effects."""
        self.food_manager.remove(food)

        # Grow the snake
        self.snake.grow(food.growth)

        # Score
        fx = food.col * GRID_SIZE + GRID_SIZE // 2
        fy = food.row * GRID_SIZE + GRID_SIZE // 2
        self.scoreboard.add_score(food.points, food.color, fx, fy)

        # Speed effects from power-ups
        if food.type == "speed":
            self.speed = max(50, self.speed - 15)
        elif food.type == "slow":
            self.speed = min(INITIAL_SPEED, self.speed + 20)

        # Visual effects
        self.particles.emit_ring(fx, fy, count=20, color=food.color, speed=5)
        self.particles.emit(fx, fy, count=8, color=food.color, spread=6)
        self.shake.trigger(4 if food.type == "mega" else 2)

        # Ensure normal food stays available
        if food.type == "normal":
            self.food_manager.spawn("normal", self.snake.positions_set)

    # ─── Rendering ───────────────────────────────────────────────────────────

    def _render(self):
        self.canvas.delete("all")
        ox = self.shake.offset_x
        oy = self.shake.offset_y

        if self.state == "menu":
            self._draw_menu()
            return

        self._draw_grid(ox, oy)
        self._draw_border(ox, oy)
        self.trail.draw(self.canvas)
        self.food_manager.draw(self.canvas, self.frame_count, ox, oy)
        self.snake.draw(self.canvas, ox, oy)
        self.particles.draw(self.canvas)

        # Flash overlay
        if self.flash_alpha > 0.01:
            flash_color = lerp_color(BG_COLOR, "#ffffff", self.flash_alpha * 0.3)
            self.canvas.create_rectangle(
                0, 0, CANVAS_WIDTH, CANVAS_HEIGHT,
                fill=flash_color, outline="", stipple="gray25"
            )

        # Score popups
        self.scoreboard.draw_popups(self.canvas, ox, oy)

        # HUD
        self.scoreboard.draw(self.canvas, self.snake.length(), self.speed)

        # Overlays
        if self.state == "paused":
            self._draw_pause()
        elif self.state == "game_over":
            self.scoreboard.draw_game_over(self.canvas, self.snake.length(), self.frame_count, self.death_reason)
            self.frame_count += 1

    def _draw_grid(self, ox, oy):
        for col in range(0, COLS + 1, 4):
            x = col * GRID_SIZE + ox
            self.canvas.create_line(x, oy, x, CANVAS_HEIGHT + oy, fill=GRID_COLOR)
        for row in range(0, ROWS + 1, 4):
            y = row * GRID_SIZE + oy
            self.canvas.create_line(ox, y, CANVAS_WIDTH + ox, y, fill=GRID_COLOR)

    def _draw_border(self, ox, oy):
        # Check wall proximity for danger warning
        col, row = self.snake.head
        wall_danger = min(col, row, COLS - 1 - col, ROWS - 1 - row)
        danger_threshold = 3

        for i in range(3):
            offset = i * 2
            alpha = 0.3 - i * 0.1
            color = lerp_color(BG_COLOR, BORDER_COLOR, alpha)
            self.canvas.create_rectangle(
                offset + ox, offset + oy,
                CANVAS_WIDTH - offset + ox, CANVAS_HEIGHT - offset + oy,
                outline=color, width=2
            )

        if wall_danger <= danger_threshold and self.state == "playing":
            # Flashing red warning border when close to wall
            intensity = (1 - wall_danger / danger_threshold)
            pulse = (math.sin(self.frame_count * 0.3) + 1) / 2
            danger_alpha = intensity * (0.5 + pulse * 0.5)
            danger_color = lerp_color(BG_COLOR, "#ff2222", danger_alpha * 0.8)
            self.canvas.create_rectangle(
                1 + ox, 1 + oy,
                CANVAS_WIDTH - 1 + ox, CANVAS_HEIGHT - 1 + oy,
                outline=danger_color, width=4
            )
        else:
            pulse = math.sin(self.frame_count * 0.05) * 0.3 + 0.7
            border_color = lerp_color(BG_COLOR, "#3344aa", pulse * 0.4)
            self.canvas.create_rectangle(
                4 + ox, 4 + oy,
                CANVAS_WIDTH - 4 + ox, CANVAS_HEIGHT - 4 + oy,
                outline=border_color, width=2
            )

    def _draw_menu(self):
        """Animated start menu."""
        # Floating background particles
        for i in range(20):
            x = (self.frame_count * (i + 1) * 0.3) % CANVAS_WIDTH
            y = (i * 47) % CANVAS_HEIGHT
            size = 3 + math.sin(self.frame_count * 0.02 + i) * 2
            color = lerp_color(BG_COLOR, "#00ff88", 0.1 + 0.05 * math.sin(i))
            self.canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill=color, outline=""
            )

        # Title
        title_y = CANVAS_HEIGHT // 3
        glow_pulse = math.sin(self.frame_count * 0.03) * 0.2 + 0.8
        glow_color = lerp_color(BG_COLOR, "#00ff88", glow_pulse * 0.3)
        self.canvas.create_text(
            CANVAS_WIDTH // 2, title_y - 3,
            text="SNEAKY 3D", fill=glow_color,
            font=("Courier", 52, "bold")
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2, title_y,
            text="SNEAKY 3D", fill="#00ff88",
            font=("Courier", 52, "bold")
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2, title_y + 50,
            text="The Ultimate Snake Experience",
            fill="#4466aa", font=("Courier", 16)
        )

        # Start prompt
        blink = ">" if int(self.frame_count * 0.05) % 2 == 0 else " "
        self.canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 40,
            text=f"{blink} Press ENTER or SPACE to Start {blink}",
            fill="#aaaacc", font=("Courier", 16, "bold")
        )

        # Controls
        controls = [
            "Arrow Keys / WASD — Move",
            "SPACE — Pause",
            "R — Restart",
        ]
        for i, line in enumerate(controls):
            self.canvas.create_text(
                CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 120 + i * 30,
                text=line, fill="#555577", font=("Courier", 13)
            )

        # Power-up legend
        legend_y = CANVAS_HEIGHT // 2 + 240
        self.canvas.create_text(
            CANVAS_WIDTH // 2, legend_y,
            text="— POWER-UPS —", fill="#666688",
            font=("Courier", 12, "bold")
        )
        power_ups = [
            ("Normal", FOOD_COLORS["normal"], "+1 pt"),
            ("Bonus", FOOD_COLORS["bonus"], "+5 pts, +3 growth"),
            ("Speed", FOOD_COLORS["speed"], "Faster"),
            ("Slow", FOOD_COLORS["slow"], "Slower"),
            ("Mega", FOOD_COLORS["mega"], "+10 pts, +5 growth"),
        ]
        for i, (name, color, desc) in enumerate(power_ups):
            y = legend_y + 25 + i * 22
            self.canvas.create_text(
                CANVAS_WIDTH // 2 - 80, y, anchor="w",
                text=name, fill=color, font=("Courier", 11, "bold")
            )
            self.canvas.create_text(
                CANVAS_WIDTH // 2 + 40, y, anchor="w",
                text=desc, fill="#555577", font=("Courier", 11)
            )

        # High score
        if self.scoreboard.high_score > 0:
            self.canvas.create_text(
                CANVAS_WIDTH // 2, CANVAS_HEIGHT - 50,
                text=f"High Score: {self.scoreboard.high_score}",
                fill="#ffaa00", font=("Courier", 14, "bold")
            )

        self.frame_count += 1

    def _draw_pause(self):
        self.canvas.create_rectangle(
            0, 0, CANVAS_WIDTH, CANVAS_HEIGHT,
            fill="#000000", stipple="gray50"
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 20,
            text="PAUSED", fill="#ffffff",
            font=("Courier", 36, "bold")
        )
        self.canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 30,
            text="Press SPACE to resume",
            fill="#aaaacc", font=("Courier", 16)
        )

    # ─── Entry Point ─────────────────────────────────────────────────────────

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()

screen.exitonclick()