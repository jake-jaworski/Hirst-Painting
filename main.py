import colorgram
import turtle
import random


def identify_colors():
    '''scrapes colors from selected image and returns list of rgb tuples'''
    colors = colorgram.extract('original_image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        color_list.append(rgb)


def paint_row():
    '''paints one 10-spot row of dots on your image'''
    for i in range(10):
        cursor.dot(20, random.choice(color_list))
        cursor.forward(50)


def next_row():
    '''moves cursor to the next row'''
    cursor.setheading(90)
    cursor.forward(50)
    cursor.setheading(180)
    cursor.forward(500)
    cursor.setheading(0)


# create arrow and screen objects
cursor = turtle.Turtle()
screen = turtle.Screen()

# sets initial conditions for the visualization
turtle.colormode(255)
cursor.speed('fast')
cursor.hideturtle()
cursor.penup()
cursor.setposition(-240, -240)
color_list = []

# scrapes a list of colors (tuples) from the provided image
identify_colors()

# generates 10x10 dotted image using random colors
for row in range(10):
    paint_row()
    next_row()

# exits program on mouse click
screen.exitonclick()
