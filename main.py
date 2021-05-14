import random
import turtle

import colorgram
from turtle import *


colors = colorgram.extract('image.jpg', 100)
color_list = []
turtle.colormode(255)


def get_color(colors):
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        c = (red, green, blue)
        color_list.append(c)


t = Turtle()
t.shape("turtle")
get_color(colors)
t.color("cyan")


def paint(c_list, dist):
    t.penup()
    t.hideturtle()
    t.goto(-200, -200)
    py = 0
    for i in range(1, 11):
        for j in range(1, 11):
            index = random.choice(c_list)
            t.dot(20, tuple(index))
            t.penup()
            t.forward(dist)
            j += 1
        i += 1
        py += dist
        t.setposition(-200, -200+py)


paint(color_list, 50)
screen = Screen()
screen.exitonclick()
