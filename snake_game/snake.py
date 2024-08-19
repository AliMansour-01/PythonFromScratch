import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments_list = []
        self.snake_body()
        self.head = self.segments_list[0]
    def snake_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments_list.append(snake)
    def extend(self):
        self.add_segment(self.segments_list[-1].position())
    def move(self):
        for i in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[i - 1].xcor()
            new_y = self.segments_list[i - 1].ycor()
            self.segments_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)