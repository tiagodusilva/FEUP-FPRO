import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("You gotta spin it to win it!")      # Set the window title

tess = turtle.Turtle()
tess.color("blue")            # Tell tess to change her color
tess.pensize(3)               # Tell tess to set her pen width

carlos = turtle.Turtle()
carlos.color("red")
carlos.pensize(3)

carlos.shape("turtle")
tess.shape("turtle")

speeeeeeeeeeed=3
while True:
    tess.left(random.uniform(-30,30))
    tess.forward(speeeeeeeeeeed)
    carlos.right(random.uniform(-30,30))
    carlos.forward(speeeeeeeeeeed)
#    speeeeeeeeeeed += 0.05
#    speeeeeeeeeeed *= 1.02
wn.mainloop()