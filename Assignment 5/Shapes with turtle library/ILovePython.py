import turtle
michelangelo = turtle.Turtle()
michelangelo.shape("turtle")
screen = turtle.Screen()
michelangelo.fillcolor("red")
michelangelo.pen(pencolor="black")
michelangelo.penup()
michelangelo.goto(0, 250)
michelangelo.pendown()
michelangelo.begin_fill()
michelangelo.left(140)
michelangelo.circle(200, 190)
michelangelo.forward(200)
michelangelo.left(50)
michelangelo.forward(220)
michelangelo.circle(200, 190)
michelangelo.end_fill()
michelangelo.penup()
michelangelo.goto(-150, 100)
michelangelo.pendown()
michelangelo.pen(pencolor="black")
michelangelo.write("I Love python", font=("Arial", 40))
michelangelo.color("darkGreen")
michelangelo.pencolor("orange")
michelangelo.turtlesize(1.5)
screen.mainloop()