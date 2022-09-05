import turtle
import random
leonardo = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
leonardo.speed(0)
color_list = ["red", "orange", "white", "green", "yellow", "pink", "blue", "violet"]


def triangle(length):
    leonardo.forward(length)
    leonardo.left(120)
    leonardo.forward(length)
    leonardo.left(120)
    leonardo.forward(length)
    leonardo.left(120)


for length in range(1000):
    color = random.choice(color_list)
    leonardo.color(color)
    triangle(length)
    leonardo.left(1)
screen.mainloop()
