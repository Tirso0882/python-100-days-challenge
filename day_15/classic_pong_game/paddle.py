from turtle import Turtle


SHAPE = "square"
COLOR = "white"
STRETCH_WIDTH = 5
STRETCH_LENGTH = 1
START_Y_POS = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(STRETCH_WIDTH, STRETCH_LENGTH)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    

        

