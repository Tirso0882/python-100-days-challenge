# 🐢 TURTLE RACING — Interactive Race Game with Visual Effects
# Features: animated track, countdown, lane labels, celebrations, replay

import random
import time
from turtle import Turtle, Screen
from art import LOGO, WINNER_ART, LOSER_ART

# --- Configuration ---
RACERS = {
    "wiki": "red",
    "roro": "blue",
    "juanfis": "green",
    "wikita": "pink",
    "barbara": "cyan",
    "diana": "yellow",
}
TRACK_LEFT = -350
TRACK_RIGHT = 340
LANE_HEIGHT = 70
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


def setup_screen():
    """Create and configure the game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("#2d2d2d")
    screen.title("🐢 TURTLE RACING CHAMPIONSHIP 🏁")
    screen.tracer(0)
    return screen


def draw_track():
    """Draw the race track with lanes, borders, and finish line."""
    track = Turtle()
    track.hideturtle()
    track.speed(0)
    track.penup()

    num_racers = len(RACERS)
    top_y = (num_racers // 2) * LANE_HEIGHT + LANE_HEIGHT // 2
    bottom_y = -top_y

    # Draw grass background
    track.goto(TRACK_LEFT - 30, top_y + 20)
    track.color("#1a472a")
    track.begin_fill()
    for _ in range(2):
        track.forward(TRACK_RIGHT - TRACK_LEFT + 60)
        track.right(90)
        track.forward(top_y - bottom_y + 40)
        track.right(90)
    track.end_fill()

    # Draw track surface
    track.goto(TRACK_LEFT - 10, top_y + 5)
    track.color("#4a4a4a")
    track.begin_fill()
    for _ in range(2):
        track.forward(TRACK_RIGHT - TRACK_LEFT + 20)
        track.right(90)
        track.forward(top_y - bottom_y + 10)
        track.right(90)
    track.end_fill()

    # Draw lane dividers (dashed white lines)
    track.color("#666666")
    track.pensize(1)
    for i in range(num_racers + 1):
        y = bottom_y + i * LANE_HEIGHT
        track.penup()
        track.goto(TRACK_LEFT, y)
        track.pendown()
        for _ in range(35):
            track.forward(10)
            track.penup()
            track.forward(10)
            track.pendown()
        track.penup()

    # Draw starting line
    track.pensize(3)
    track.color("white")
    track.penup()
    track.goto(TRACK_LEFT + 20, top_y + 5)
    track.pendown()
    track.goto(TRACK_LEFT + 20, bottom_y - 5)
    track.penup()

    # Draw finish line (checkered pattern)
    square_size = 10
    for row in range(num_racers * LANE_HEIGHT // square_size + 1):
        for col in range(3):
            x = TRACK_RIGHT - col * square_size
            y = bottom_y + row * square_size
            if (row + col) % 2 == 0:
                track.goto(x, y)
                track.color("white")
                track.begin_fill()
                for _ in range(4):
                    track.forward(square_size)
                    track.right(90)
                track.end_fill()
            else:
                track.goto(x, y)
                track.color("black")
                track.begin_fill()
                for _ in range(4):
                    track.forward(square_size)
                    track.right(90)
                track.end_fill()


def draw_lane_labels():
    """Write racer names next to their lanes."""
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.speed(0)

    names = list(RACERS.keys())
    num_racers = len(names)
    start_y = -((num_racers - 1) / 2) * LANE_HEIGHT

    for i, name in enumerate(names):
        y = start_y + i * LANE_HEIGHT
        color = RACERS[name]
        writer.goto(TRACK_LEFT - 50, y - 10)
        writer.color(color)
        writer.write(name.upper(), align="right", font=("Courier", 11, "bold"))


def draw_title():
    """Draw the game title at the top."""
    title = Turtle()
    title.hideturtle()
    title.penup()
    title.goto(0, SCREEN_HEIGHT // 2 - 50)
    title.color("gold")
    title.write("🐢 TURTLE RACING CHAMPIONSHIP 🏁",
                align="center", font=("Courier", 18, "bold"))


def create_racer(color, y_pos):
    """Create a racing turtle at the starting position."""
    t = Turtle(shape="turtle")
    t.shapesize(stretch_wid=1.5, stretch_len=1.5)
    t.color(color)
    t.penup()
    t.goto(TRACK_LEFT + 30, y_pos)
    return t


def countdown(screen):
    """Display a 3-2-1-GO countdown animation."""
    counter = Turtle()
    counter.hideturtle()
    counter.penup()
    counter.goto(0, 0)

    for text, color in [("3", "red"), ("2", "orange"), ("1", "yellow"), ("GO!", "lime")]:
        counter.color(color)
        counter.write(text, align="center", font=("Courier", 60, "bold"))
        screen.update()
        time.sleep(0.7)
        counter.clear()

    screen.update()


def celebrate_winner(winner_turtle, screen):
    """Animate the winning turtle with a victory dance."""
    original_size = winner_turtle.shapesize()

    for _ in range(3):
        # Grow
        winner_turtle.shapesize(stretch_wid=2.5, stretch_len=2.5)
        screen.update()
        time.sleep(0.15)
        # Shrink
        winner_turtle.shapesize(stretch_wid=1.5, stretch_len=1.5)
        screen.update()
        time.sleep(0.15)

    # Spin celebration
    for _ in range(4):
        winner_turtle.right(90)
        screen.update()
        time.sleep(0.1)

    winner_turtle.shapesize(*original_size)


def show_result(screen, winning_name, user_bet):
    """Display the race result on screen."""
    result = Turtle()
    result.hideturtle()
    result.penup()
    result.goto(0, -20)

    if winning_name.lower().strip() == user_bet.lower().strip():
        result.color("lime")
        result.write(f"🎉 YOU WIN! {winning_name.upper()} takes it! 🎉",
                     align="center", font=("Courier", 16, "bold"))
        print(WINNER_ART)
    else:
        result.color("tomato")
        result.write(f"💀 {winning_name.upper()} wins! You bet on {user_bet}... 💀",
                     align="center", font=("Courier", 14, "bold"))
        print(LOSER_ART)

    # Replay prompt
    result.goto(0, -60)
    result.color("white")
    result.write("Click anywhere to exit", align="center",
                 font=("Courier", 12, "normal"))
    screen.update()


def draw_dust_trail(racer, screen):
    """Occasionally stamp a small dust particle behind a racer."""
    if random.random() < 0.08:
        dust = Turtle()
        dust.hideturtle()
        dust.penup()
        dust.shape("circle")
        dust.shapesize(0.2, 0.2)
        dust.color("#8b7355")
        dust.goto(racer.xcor() - 15, racer.ycor() + random.randint(-5, 5))
        dust.showturtle()
        dust.stamp()
        dust.hideturtle()


def run_race():
    """Main game loop."""
    print(LOGO)

    screen = setup_screen()

    # Draw the environment
    draw_track()
    draw_lane_labels()
    draw_title()
    screen.update()

    # Get player bet
    names_list = ", ".join(RACERS.keys())
    user_bet = screen.textinput(
        title="🐢 Place Your Bet!",
        prompt=f"Who will win?\nRacers: {names_list}\n\nEnter a name:"
    )

    if not user_bet:
        screen.bye()
        return

    # Validate bet
    if user_bet.lower().strip() not in RACERS:
        user_bet = screen.textinput(
            title="⚠️ Invalid name!",
            prompt=f"Choose from: {names_list}\n\nEnter a name:"
        )
        if not user_bet or user_bet.lower().strip() not in RACERS:
            screen.bye()
            return

    # Show bet confirmation
    bet_display = Turtle()
    bet_display.hideturtle()
    bet_display.penup()
    bet_display.goto(0, -(SCREEN_HEIGHT // 2) + 30)
    bet_display.color("white")
    bet_display.write(f"💰 Your bet: {user_bet.upper()} 💰",
                      align="center", font=("Courier", 12, "bold"))
    screen.update()

    # Create racer turtles
    racer_list = []
    names = list(RACERS.keys())
    num_racers = len(names)
    start_y = -((num_racers - 1) / 2) * LANE_HEIGHT

    for i, name in enumerate(names):
        y = start_y + i * LANE_HEIGHT
        t = create_racer(RACERS[name], y)
        racer_list.append((name, t))

    screen.update()
    time.sleep(0.5)

    # Countdown
    countdown(screen)

    # Race loop
    race_is_on = True
    frame_count = 0

    while race_is_on:
        frame_count += 1

        for name, racer in racer_list:
            # Variable speed with bursts
            if random.random() < 0.1:
                distance = random.randint(0, 5)  # Speed burst!
            else:
                distance = random.randint(1, 3)

            racer.forward(distance)

            # Check for winner
            if racer.xcor() >= TRACK_RIGHT - 30:
                race_is_on = False
                celebrate_winner(racer, screen)
                show_result(screen, name, user_bet)
                break

        screen.update()
        time.sleep(0.02)

    screen.exitonclick()


if __name__ == "__main__":
    run_race()
