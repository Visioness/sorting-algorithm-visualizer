from turtle import *

# Default Turtle size in pixels
TURTLE_SIZE = 20

class Block(Turtle):
    def __init__(self, len_coef, xcor, wid_coef):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        
        # Stretching its length based on the magnitude of the element
        # Stretching its width based on the size of the array
        self.shapesize(stretch_len=len_coef, stretch_wid=wid_coef)
        self.turtle_length, self.turtle_width = ((TURTLE_SIZE * len_coef), TURTLE_SIZE * wid_coef)
        self.penup()
        
        # Setting the position of the block with given xcor
        self.goto(xcor, (-430 + self.turtle_length / 2))