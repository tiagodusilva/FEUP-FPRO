##!/usr/bin/env python3

import turtle

turtle.setup(500, 500)
wn = turtle.Screen()

clock = turtle.Turtle()
clock.speed(0)
clock.color("blue")
clock.shape("turtle")
clock.pensize(2)

for _ in range(12):
    clock.penup()
    clock.forward(100)
    clock.pendown()
    clock.forward(30)
    clock.penup()
    clock.forward(20)
    clock.stamp()
    clock.backward(150)
    clock.left(360 / 12)

clock.left(90)

wn.mainloop()
