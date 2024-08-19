from turtle import Turtle

PADDLE_MOVEMENT = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

