from turtle import Turtle,Screen
import time
from Snake import snake
from food import Food
sc=Screen()

sc.setup(width=900, height=700)
sc.bgcolor("purple")
sc.title("Snake Game")
sc.tracer(0)
sk=snake()
fd=Food()
sk.build_snake()


is_on=True
sc.listen()
sc.onkey(fun=sk.move_up,key="Up")
sc.onkey(fun=sk.move_left,key="Left")
sc.onkey(fun=sk.move_right,key="Right")
sc.onkey(fun=sk.move_down,key="Down")
while is_on:
    sc.update()
    time.sleep(0.1)
    if sk.head.distance(fd)<18:
        fd.refresh()
        sk.inc_snake()
    sk.move_snake()

    if sk.head.xcor()>540 or sk.head.xcor()<-540 or sk.head.ycor()>340 or sk.head.ycor()<-340:
        is_on=False

    if sk.check_collision_tail():
        is_on=False


sc.exitonclick()

