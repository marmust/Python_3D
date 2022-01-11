# imports
import turtle
import time
# imports
# parameters
height = 1
width = 1
x = 1
turtle.bgcolor("grey")
# parameters
# main loop
while x == 1:
    # sub main cycle 1
    for i in range(5):
        turtle.clear()
        turtle.hideturtle()
        width = width - 0.2
        turtle.speed(0)
        turtle.pendown()
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(-100 * width, -100 * height)
        turtle.pendown()
        turtle.goto(-100 * width, 100 * height)
        turtle.goto(100 * width, 100 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.fillcolor("green")
        turtle.penup()
        turtle.goto(100 * width, 100 * height)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(200 * width, 0 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.end_fill()
        turtle.penup()
        time.sleep(0.1)
    # sub main cycle 1
    # sub main cycle 2
    for k in range(5):
        turtle.clear()
        turtle.hideturtle()
        width = width + 0.2
        turtle.speed(0)
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(-100 * width, -100 * height)
        turtle.pendown()
        turtle.goto(-100 * width, 100 * height)
        turtle.goto(100 * width, 100 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.fillcolor("green")
        turtle.penup()
        turtle.goto(-100 * width, 100 * height)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(-200 * width, 0 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.penup()
        time.sleep(0.1)
    # sub main cycle 2
    # sub main cycle 3
    for i in range(5):
        turtle.clear()
        turtle.hideturtle()
        width = width - 0.2
        turtle.speed(0)
        turtle.pendown()
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(-100 * width, -100 * height)
        turtle.pendown()
        turtle.goto(-100 * width, 100 * height)
        turtle.goto(100 * width, 100 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.fillcolor("green")
        turtle.penup()
        turtle.goto(-100 * width, 100 * height)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(-200 * width, 0 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.penup()
        time.sleep(0.1)
    # sub main cycle 3
    # sub main cycle 4
    for i in range(5):
        turtle.clear()
        turtle.hideturtle()
        width = width + 0.2
        turtle.speed(0)
        turtle.pendown()
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(-100 * width, -100 * height)
        turtle.pendown()
        turtle.goto(-100 * width, 100 * height)
        turtle.goto(100 * width, 100 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.goto(-100 * width, -100 * height)
        turtle.end_fill()
        turtle.fillcolor("green")
        turtle.penup()
        turtle.goto(100 * width, 100 * height)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(200 * width, 0 * height)
        turtle.goto(100 * width, -100 * height)
        turtle.end_fill()
        turtle.penup()
        time.sleep(0.1)
    # sub main cycle 4
# main loop