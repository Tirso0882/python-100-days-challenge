from turtle import Turtle, Screen
import random

COLOR_LIST = ["green", "red", "blue", "magenta", "cyan", "pink", "orange", "LimeGreen"]

screen = Screen()
screen.title("Polygon Drawer")
screen.bgcolor("black")
screen.setup(width=800, height=600)

pen = Turtle()
pen.shape("turtle")
pen.speed(3)


def draw_polygon(n_sides, side_length):
    """Draw a regular polygon with the given number of sides and side length."""
    pen.color(random.choice(COLOR_LIST))
    angle = 360 / n_sides
    for _ in range(n_sides):
        pen.forward(side_length)
        pen.right(angle)


def get_sides():
    """Ask user for number of sides via dialog box (must be >= 3)."""
    while True:
        n_sides = screen.numinput(
            title="Number of sides",
            prompt="How many sides? (3 or more, cancel to quit)",
            minval=3,
            maxval=100,
        )
        if n_sides is None:
            return None
        return int(n_sides)


def get_length():
    """Ask user for side length via dialog box (must be > 0)."""
    while True:
        length = screen.numinput(
            title="Side length",
            prompt="How long should each side be? (10 – 300)",
            minval=10,
            maxval=300,
        )
        if length is None:
            return None
        return int(length)


def prompt_clear():
    """Ask if the user wants to clear the canvas."""
    answer = screen.textinput(
        title="Clear canvas?",
        prompt="Clear the canvas? (yes / no)",
    )
    if answer is not None and answer.strip().lower() in ("yes", "y"):
        pen.clear()
        pen.home()


def run():
    """Main loop: keep asking for shapes until the user cancels."""
    while True:
        n_sides = get_sides()
        if n_sides is None:
            break

        side_length = get_length()
        if side_length is None:
            break

        draw_polygon(n_sides, side_length)
        prompt_clear()

    screen.bye()


run()

