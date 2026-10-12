import time
from ball import Ball
from paddle import Paddle

from turtle import Screen

# 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Pong Game")
screen.tracer(0)

# 2. Create and move a. paddle_1, b. paddle_2
paddle_left = Paddle((450, 0))
paddle_right = Paddle((-450, 0))
# 3. Create and move the ball
ball = Ball()

screen.onkey(paddle_left.go_up, "Up")
screen.onkey(paddle_left.go_down, "Down")
screen.onkey(paddle_right.go_up, "w")
screen.onkey(paddle_right.go_down, "s")

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
# def move_ball():




screen.exitonclick()



# 4. Detect collision with wall and paddles
# 5. Detect when paddle misses
# 6. Keep score

