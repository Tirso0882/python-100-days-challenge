"""Food system with multiple power-up types and 3D rendering."""

import math
import random

from config import (
    COLS, ROWS, GRID_SIZE, BG_COLOR,
    FOOD_COLORS, FOOD_SYMBOLS,
)
from utils import lerp_color, darken_color, brighten_color


# Food type configurations: (lifetime_frames, points, growth_amount)
FOOD_CONFIG = {
    "normal": (None, 1, 1),
    "bonus":  (80, 5, 3),
    "speed":  (100, 2, 1),
    "slow":   (100, 2, 1),
    "mega":   (60, 10, 5),
}


class FoodItem:
    """A single food item with a type, position, and lifetime."""

    def __init__(self, food_type="normal"):
        self.type = food_type
        self.col = 0
        self.row = 0
        self.pulse_phase = random.uniform(0, 2 * math.pi)
        self.spawn_time = 0

        config = FOOD_CONFIG.get(food_type, FOOD_CONFIG["normal"])
        self.lifetime = config[0]
        self.points = config[1]
        self.growth = config[2]

    @property
    def color(self):
        return FOOD_COLORS.get(self.type, FOOD_COLORS["normal"])

    @property
    def symbol(self):
        return FOOD_SYMBOLS.get(self.type, "●")

    @property
    def position(self):
        return (self.col, self.row)

    def place(self, occupied_positions):
        """Place food at a random position not in occupied_positions.
        Food spawns at least 5 cells from any wall to give the player room to turn."""
        buffer = 5
        while True:
            self.col = random.randint(buffer, COLS - 1 - buffer)
            self.row = random.randint(buffer, ROWS - 1 - buffer)
            if (self.col, self.row) not in occupied_positions:
                break
        self.spawn_time = 0

    def tick(self):
        """Advance the spawn timer by one frame."""
        self.spawn_time += 1

    def is_expired(self):
        """Return True if this food has exceeded its lifetime."""
        if self.lifetime is None:
            return False
        return self.spawn_time >= self.lifetime

    def draw(self, canvas, frame_count, offset_x=0, offset_y=0):
        """Render the food with 3D glow and pulsing animation."""
        x = self.col * GRID_SIZE + offset_x
        y = self.row * GRID_SIZE + offset_y
        cx = x + GRID_SIZE // 2
        cy = y + GRID_SIZE // 2

        # Pulsing size
        pulse = math.sin(frame_count * 0.1 + self.pulse_phase) * 0.2 + 1.0
        size = (GRID_SIZE // 2 - 2) * pulse

        # Lifetime ring (fades as food expires)
        if self.lifetime:
            remaining = 1 - (self.spawn_time / self.lifetime)
            ring_size = size + 8 * remaining
            ring_color = lerp_color(BG_COLOR, self.color, remaining * 0.3)
            canvas.create_oval(
                cx - ring_size, cy - ring_size,
                cx + ring_size, cy + ring_size,
                outline=ring_color, width=2
            )

        # Outer glow
        glow_size = size + 4
        glow_color = lerp_color(BG_COLOR, self.color, 0.3)
        canvas.create_oval(
            cx - glow_size, cy - glow_size,
            cx + glow_size, cy + glow_size,
            fill=glow_color, outline=""
        )

        # Shadow
        canvas.create_oval(
            cx - size + 3, cy - size + 5,
            cx + size + 3, cy + size + 5,
            fill=darken_color(self.color, 0.2), outline=""
        )

        # Main body
        canvas.create_oval(
            cx - size, cy - size,
            cx + size, cy + size,
            fill=self.color, outline=darken_color(self.color, 0.7)
        )

        # 3D highlight
        hl_size = size * 0.4
        canvas.create_oval(
            cx - size * 0.4, cy - size * 0.4,
            cx - size * 0.4 + hl_size, cy - size * 0.4 + hl_size,
            fill=brighten_color(self.color, 1.6), outline=""
        )

        # Type symbol
        canvas.create_text(
            cx, cy + 1, text=self.symbol,
            fill="#ffffff", font=("Courier", 10, "bold")
        )


class FoodManager:
    """Manages spawning, expiration, and collision of all food items."""

    def __init__(self):
        self.items = []

    def reset(self):
        self.items.clear()

    def spawn(self, food_type, snake_positions):
        """Create and place a new food item."""
        food = FoodItem(food_type)
        food.place(snake_positions)
        self.items.append(food)

    def update(self, snake_positions):
        """Tick timers, expire old food, ensure normal food exists."""
        for food in self.items[:]:
            food.tick()
            if food.is_expired():
                self.items.remove(food)

        # Always keep at least one normal food on the field
        if not any(f.type == "normal" for f in self.items):
            self.spawn("normal", snake_positions)

    def check_collision(self, head_position):
        """Check if head is on any food. Returns the FoodItem or None."""
        for food in self.items:
            if head_position == food.position:
                return food
        return None

    def remove(self, food):
        """Remove a food item from the manager."""
        if food in self.items:
            self.items.remove(food)

    def spawn_random_powerup(self, snake_positions):
        """Spawn a random power-up type."""
        power_type = random.choices(
            ["bonus", "speed", "slow", "mega"],
            weights=[40, 25, 25, 10]
        )[0]
        self.spawn(power_type, snake_positions)

    def draw(self, canvas, frame_count, offset_x=0, offset_y=0):
        """Render all food items."""
        for food in self.items:
            food.draw(canvas, frame_count, offset_x, offset_y)
