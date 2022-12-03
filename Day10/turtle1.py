#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
