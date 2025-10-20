from turtle import Turtle
from typing import List, Any

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cords in START_POSITION:
            print(f"in snake cords: {cords}")
            self.add_segment(cords)

    def add_segment(self, position):
        block = Turtle('square')
        block.penup()
        block.color('red')
        block.goto(position)
        self.segments.append(block)

    def extend(self):
        last_pos = self.segments[-1].position()
        self.add_segment(last_pos)

    def move(self):

        for it in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[it - 1].xcor()
            new_y = self.segments[it - 1].ycor()
            self.segments[it].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # if self.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.segments:
            seg.goto(800,800)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
