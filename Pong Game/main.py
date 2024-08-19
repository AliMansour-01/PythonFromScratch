from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def create_screen(screen):
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen

def listen(screen):
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")


screen = Screen()
score = Scoreboard()
create_screen(screen)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    listen(screen)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect R paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_score()
    # Detect L paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_score()
screen.exitonclick()