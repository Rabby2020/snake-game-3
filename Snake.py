from turtle import Screen,Turtle
import time
sc=Screen()
class snake:
    segments=[]
    shift = 0
    def build_snake(self):
        sc.tracer(0)
        for x in range(3):
            segment = Turtle("square")
            segment.penup()
            self.segments.append(segment)
            segment.color("white")
            segment.goto(self.shift, 0)
            self.shift -= 20
        self.head=self.segments[0]
        # sc.update()
        # time.sleep(1)

    def inc_snake(self):
        segment=Turtle("square")
        segment.penup()
        self.segments.append(segment)
        segment.color("white")
        segment.goto(self.shift,0)
        self.shift-=20

    def check_collision_tail(self):
        checker=False
        for segment in self.segments:
            if segment==self.head:
                continue
            if self.head.distance(segment)<10:
                checker=True
        return checker

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.segments[0].forward(20)
        #sc.update()
        #time.sleep(0.1)

    def move_left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


