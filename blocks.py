from turtle import *

TURTLE_SIZE = 20
STRETCH_COEF = 0.5

class Block(Turtle):
    def __init__(self, len_coef, xcor):
        super().__init__()
        self.setheading(90)
        self.shape('square')
        self.shapesize(stretch_len=STRETCH_COEF + (STRETCH_COEF * len_coef), stretch_wid=0.5)
        self.turtle_length, self.turtle_width = ((TURTLE_SIZE * STRETCH_COEF * len_coef), TURTLE_SIZE)
        self.penup()
        self.color('white')
        self.goto(xcor, (-430 + self.turtle_length / 2))