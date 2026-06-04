"""Game configuration constants."""

# ─── Window ──────────────────────────────────────────────────────────────────
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
GRID_SIZE = 20
COLS = CANVAS_WIDTH // GRID_SIZE
ROWS = CANVAS_HEIGHT // GRID_SIZE

# ─── Speed ───────────────────────────────────────────────────────────────────
INITIAL_SPEED = 120  # ms per frame
MIN_SPEED = 50
SPEED_INCREMENT = 2

# ─── Colors ──────────────────────────────────────────────────────────────────
BG_COLOR = "#0a0a1a"
GRID_COLOR = "#111128"
BORDER_COLOR = "#2a2a5a"

SNAKE_HEAD_COLOR = "#00ff88"
SNAKE_TAIL_COLOR = "#005522"
SNAKE_SHADOW_COLOR = "#003311"
SNAKE_EYE_COLOR = "#ffffff"
SNAKE_PUPIL_COLOR = "#000000"

FOOD_COLORS = {
    "normal": "#ff3366",
    "bonus": "#ffaa00",
    "speed": "#00ccff",
    "slow": "#aa44ff",
    "mega": "#ff00ff",
}

FOOD_SYMBOLS = {
    "normal": "●",
    "bonus": "★",
    "speed": "⚡",
    "slow": "❄",
    "mega": "◆",
}

PARTICLE_COLORS = ["#ff3366", "#ffaa00", "#00ff88", "#00ccff", "#ff00ff", "#ffffff"]
