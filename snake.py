from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.up()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(0)
