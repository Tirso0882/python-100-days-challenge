from turtle import Turtle


SHAPE = "circle"
COLOR = "white"
STRETCH_WIDTH = 1.0
STRETCH_LENGTH = 1.0
X_MAX = 500
Y_MAX = 400


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        
        # self.shapesize(STRETCH_WIDTH, STRETCH_LENGTH)
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        # for i in range(0, X_MAX):
        #     if new_x > X_MAX:
        #         print("You lose!")
        #     new_x += 20
        #     for j in range(0, Y_MAX):
        #         if new_y > Y_MAX:
        #             print("You lose!")
        #         new_y += 20
