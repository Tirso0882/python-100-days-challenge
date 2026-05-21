import turtle
import random

# Config variables
num_steps = 200
step_size = 30

# Fix angles 
fix_directions = [0, 90, 180, 270]  # grid-aligned walk

# Organic curves
curves_directions = [i for i in range(0, 361)]  # 0 to 360 degrees
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
pen_size = 20
speed = "fast"

t = turtle.Turtle()
t.pensize(pen_size)
t.speed(speed)

for _ in range(num_steps):
    t.color(random.choice(colors))
    t.forward(step_size)
    t.setheading(random.choice(fix_directions))