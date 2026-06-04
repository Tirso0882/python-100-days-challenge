"""Visual effects: particles, screen shake, and trail."""

import math
import random
from collections import deque

from config import BG_COLOR, PARTICLE_COLORS
from utils import lerp_color


class Particle:
    """A single animated particle with physics."""

    def __init__(self, x, y, color=None, vx=None, vy=None, life=None, size=None):
        self.x = x
        self.y = y
        self.color = color or random.choice(PARTICLE_COLORS)
        self.vx = vx if vx is not None else random.uniform(-4, 4)
        self.vy = vy if vy is not None else random.uniform(-4, 4)
        self.life = life or random.uniform(0.4, 1.0)
        self.max_life = self.life
        self.size = size or random.uniform(2, 6)
        self.gravity = 0.15

    def update(self, dt):
        """Update position and return True if still alive."""
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.life -= dt
        return self.life > 0

    @property
    def alpha(self):
        return max(0, self.life / self.max_life)


class ParticleSystem:
    """Manages a collection of particles with burst/ring emission patterns."""

    def __init__(self):
        self.particles = []

    def emit(self, x, y, count=10, color=None, spread=4, life=None, size=None):
        """Emit particles in a random burst."""
        for _ in range(count):
            vx = random.uniform(-spread, spread)
            vy = random.uniform(-spread, spread)
            self.particles.append(
                Particle(x, y, color=color, vx=vx, vy=vy, life=life, size=size)
            )

    def emit_ring(self, x, y, count=16, color=None, speed=3, life=None):
        """Emit particles in an expanding ring pattern."""
        for i in range(count):
            angle = (2 * math.pi * i) / count
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(
                Particle(x, y, color=color, vx=vx, vy=vy, life=life or 0.6, size=3)
            )

    def update(self, dt):
        """Advance all particles and remove dead ones."""
        self.particles = [p for p in self.particles if p.update(dt)]

    def draw(self, canvas):
        """Render all particles onto the canvas."""
        for p in self.particles:
            alpha = p.alpha
            size = p.size * alpha
            if size < 0.5:
                continue
            color = lerp_color(p.color, BG_COLOR, 1 - alpha)
            canvas.create_oval(
                p.x - size, p.y - size,
                p.x + size, p.y + size,
                fill=color, outline=""
            )


class ScreenShake:
    """Applies camera shake with exponential decay."""

    def __init__(self):
        self.intensity = 0
        self.decay = 0.85
        self.offset_x = 0
        self.offset_y = 0

    def trigger(self, intensity=8):
        self.intensity = intensity

    def update(self):
        if self.intensity > 0.5:
            self.offset_x = random.uniform(-self.intensity, self.intensity)
            self.offset_y = random.uniform(-self.intensity, self.intensity)
            self.intensity *= self.decay
        else:
            self.intensity = 0
            self.offset_x = 0
            self.offset_y = 0


class Trail:
    """Fading trail behind the snake head."""

    def __init__(self, max_length=40):
        self.positions = deque(maxlen=max_length)

    def add(self, x, y):
        self.positions.append((x, y))

    def clear(self):
        self.positions.clear()

    def draw(self, canvas):
        length = len(self.positions)
        for i, (x, y) in enumerate(self.positions):
            alpha = i / max(1, length)
            size = 2 + alpha * 3
            color = lerp_color(BG_COLOR, "#004422", alpha * 0.6)
            canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill=color, outline=""
            )
