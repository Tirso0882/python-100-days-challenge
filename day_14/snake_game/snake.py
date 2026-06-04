"""Snake class — manages position, movement, growth, and 3D rendering."""

from config import (
    COLS, ROWS, GRID_SIZE,
    SNAKE_HEAD_COLOR, SNAKE_TAIL_COLOR,
    SNAKE_SHADOW_COLOR, SNAKE_EYE_COLOR, SNAKE_PUPIL_COLOR,
)
from utils import lerp_color, darken_color, brighten_color


STARTING_POSITIONS = [(COLS // 2 - i, ROWS // 2) for i in range(4)]

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Opposite direction mapping (to prevent 180-degree reversal)
OPPOSITES = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}


class Snake:
    """The player-controlled snake with grid-based movement."""

    def __init__(self):
        self.segments = list(STARTING_POSITIONS)
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.growing = 0
        self._input_queue = []

    @property
    def head(self):
        return self.segments[0]

    @property
    def body(self):
        return self.segments[1:]

    @property
    def positions_set(self):
        return set(self.segments)

    def reset(self):
        """Reset snake to starting state."""
        self.segments = list(STARTING_POSITIONS)
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.growing = 0
        self._input_queue = []

    def set_direction(self, new_direction):
        """Queue a direction change. Only one direction per frame is applied,
        preventing rapid key presses from creating effective 180-degree turns."""
        self._input_queue.append(new_direction)

    def move(self):
        """
        Advance the snake by one grid cell.
        Returns the new head position.
        """
        # Process input queue: accept the first valid direction change
        for queued_dir in self._input_queue:
            if queued_dir != OPPOSITES.get(self.direction):
                self.next_direction = queued_dir
                break
        self._input_queue.clear()

        self.direction = self.next_direction
        head_col, head_row = self.head
        dx, dy = self.direction
        new_head = (head_col + dx, head_row + dy)

        # Insert new head
        self.segments.insert(0, new_head)

        # Handle tail: if growing, keep tail; otherwise remove it
        if self.growing > 0:
            self.growing -= 1
        else:
            self.segments.pop()

        return new_head

    def grow(self, amount=1):
        """Queue growth segments."""
        self.growing += amount

    def check_wall_collision(self):
        """Return True if head is out of bounds."""
        col, row = self.head
        return col < 0 or col >= COLS or row < 0 or row >= ROWS

    def check_self_collision(self):
        """Return True if head overlaps any body segment."""
        return self.head in set(self.segments[1:])

    def length(self):
        return len(self.segments)

    def draw(self, canvas, offset_x=0, offset_y=0):
        """Render the snake with 3D shading, gradient, and eyes."""
        total = len(self.segments)

        # Draw from tail to head so head is on top
        for i in range(total - 1, -1, -1):
            col, row = self.segments[i]
            x = col * GRID_SIZE + offset_x
            y = row * GRID_SIZE + offset_y

            # Gradient color from head to tail
            t = i / max(1, total - 1)
            body_color = lerp_color(SNAKE_HEAD_COLOR, SNAKE_TAIL_COLOR, t)

            # Shadow (offset below and right)
            canvas.create_oval(
                x + 5, y + 5,
                x + GRID_SIZE + 1, y + GRID_SIZE + 1,
                fill=SNAKE_SHADOW_COLOR, outline=""
            )

            # Main body segment
            canvas.create_oval(
                x + 1, y + 1,
                x + GRID_SIZE - 1, y + GRID_SIZE - 1,
                fill=body_color,
                outline=darken_color(body_color, 0.7)
            )

            # 3D highlight (top-left shine)
            hl_size = GRID_SIZE // 3
            canvas.create_oval(
                x + 3, y + 3,
                x + 3 + hl_size, y + 3 + hl_size,
                fill=brighten_color(body_color, 1.4), outline=""
            )

        # Eyes on head
        if total > 0:
            self._draw_eyes(canvas, offset_x, offset_y)

    def _draw_eyes(self, canvas, ox, oy):
        """Draw directional eyes on the head."""
        col, row = self.head
        cx = col * GRID_SIZE + GRID_SIZE // 2 + ox
        cy = row * GRID_SIZE + GRID_SIZE // 2 + oy
        dx, dy = self.direction

        eye_offset = 5
        eye_size = 4
        pupil_size = 2

        # Position eyes based on facing direction
        if dx == 1:
            eyes = [(cx + eye_offset, cy - 4), (cx + eye_offset, cy + 4)]
        elif dx == -1:
            eyes = [(cx - eye_offset, cy - 4), (cx - eye_offset, cy + 4)]
        elif dy == -1:
            eyes = [(cx - 4, cy - eye_offset), (cx + 4, cy - eye_offset)]
        else:
            eyes = [(cx - 4, cy + eye_offset), (cx + 4, cy + eye_offset)]

        for ex, ey in eyes:
            canvas.create_oval(
                ex - eye_size, ey - eye_size,
                ex + eye_size, ey + eye_size,
                fill=SNAKE_EYE_COLOR, outline=""
            )
            canvas.create_oval(
                ex - pupil_size + dx, ey - pupil_size + dy,
                ex + pupil_size + dx, ey + pupil_size + dy,
                fill=SNAKE_PUPIL_COLOR, outline=""
            )