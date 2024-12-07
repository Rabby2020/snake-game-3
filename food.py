from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.8,stretch_len=0.8)
        self.penup()
        self.refresh()

    def refresh(self):
        x=random.randint(-420,420)
        y=random.randint(-320,320)
        self.goto(x,y)


