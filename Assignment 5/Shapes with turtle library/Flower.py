import turtle
leonardo = turtle.Turtle()
window = turtle.Screen()
leonardo.speed(0)
leonardo.color("Red")
for j in range(6):
    for i in range(0, 120):
        leonardo.circle(190-i, 90)
        leonardo.left(90)
        leonardo.circle(190-i, 90)
        leonardo.left(90)
    leonardo.left(60)
window.mainloop()
