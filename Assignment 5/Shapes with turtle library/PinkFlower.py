import turtle
raphael = turtle.Turtle()
window = turtle.Screen()
raphael.speed(0)
raphael.color("Green", )
raphael.pen(pensize=5)
for i in range(250):
    if 190 - i < 0:
        raphael.color("#FF1493")
        raphael.pen(pensize=10)
    raphael.circle(190 - i, 90)
    raphael.left(90)
    raphael.circle(190 - i, 90)
    raphael.left(18)

window.mainloop()
