import random
from turtle import Turtle



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(x=random_x, y=random_y)
