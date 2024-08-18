import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_guess = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []

race_is_on = False
y_axis = -90

if user_guess:
    race_is_on = True

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_axis)
    y_axis += 30
    turtles_list.append(new_turtle)

while race_is_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner. ")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner. ")
        distance = random.randint(1,10)
        turtle.forward(distance)


screen.exitonclick()