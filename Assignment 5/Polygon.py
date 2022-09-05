import tkinter
import turtle
numberOfSides = int(input("Enter the number of sides: "))
color = input("Enter the color: ")
if numberOfSides < 3:
    print("The number of sides must be more than three.")
else:
    leonardo = turtle.Turtle()
    screen = turtle.Screen()
    angle = ((numberOfSides-2) * 180)/numberOfSides
    print(angle)
    try:
        leonardo.pen(pencolor=color)
        for i in range(numberOfSides):
            leonardo.forward(100)
            leonardo.left(180-angle)

    except tkinter.TclError:
        print("Enter the color correctly.")

    screen.mainloop()
