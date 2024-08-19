from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

def create_screen():
    s = Screen()
    s.setup(600, 600)
    s.bgcolor("black")
    s.title("The snake game")
    s.tracer(0)
    return s
def screen_listen(s, snake):
    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.right, "Right")
    s.onkey(snake.left, "Left")

snake = Snake()
food = Food()
scoreboard = Score()

screen = create_screen()
screen_listen(screen, snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.update_score()
screen.exitonclick()