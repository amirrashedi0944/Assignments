import turtle
raphael = turtle.Turtle()
raphael.speed(10)
for i in range(360):
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
    raphael.left(90)
    raphael.left(1)
turtle.Screen()
turtle.mainloop()