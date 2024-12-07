import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.x=0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,315)
        self.write(arg=f"score: {self.x}",move=False,align="center",font=("Arial",20,"normal"))

    def inc(self):
        self.x+=1
        self.clear()
        self.write(arg=f"score: {self.x}",move=False,align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over!", move=False, align="center", font=("Arial", 24, "normal"))