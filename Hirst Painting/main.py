import random
import turtle
from turtle import Turtle, Screen
import decimal


#import colorgram
#
#colors = colorgram.extract('image.jpg', 30)
#rgb_colors = []
#
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
turtle.colormode(255)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
tim.speed("fastest")

tim.penup()
tim.setheading(215)
tim.forward(300)
tim.setheading(0)


x_axis = round(tim.xcor(), 2)
y_axis = round(tim.ycor(), 2)

num_of_dots = 100
for i in range(1, num_of_dots + 1):
    tim.penup()
    tim.dot(20, random.choice(color_list)), tim.fd(50)
    if i % 10 == 0:
        y_axis += 50
        tim.setposition(x_axis, y_axis)
    if i == 100:
        keep_running = False

screen = Screen()
screen.exitonclick()