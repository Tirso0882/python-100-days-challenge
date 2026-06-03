# Plan:
# step 1: Create the snake body
# step 2: Move the snake
# Step 3: Control the snake using the arrow keys to move it across the screen
# Step 4: Create the food for the snake and detect when the snake eats the food
# Step 5: Create a scoreboard to keep track of the score
# Step6: when the game ends and snake should no longer move:
#     - Detect when the snake collides with the wall or itself
#     - Display a game over message and the final score
#     - Optionally, provide an option to restart the game or exit


# Building up the game...

import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen



screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Sneaky")
screen.tracer(0)

# step 1: Create the snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Step 3: Control the snake using the arrow keys to move it across the screen        
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# step 2: Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(move_unit=20)

    # Step 4: Create the food for the snake and detect when the snake eats the food
    # a. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_snake()
        scoreboard.increase_score()
        
        


  

screen.exitonclick()