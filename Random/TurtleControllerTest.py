import turtle

def turn_Right():
    skane.right(10)
    return

def turn_Left():
    skane.left(10)
    return

wn = turtle.Screen()
wn.bgcolor("Green")
wn.title("A walk in the park")

skane = turtle.Turtle()
skane.shape("classic")
skane.shapesize(2.5,2.5,0)
skane.color("DarkBlue")
skane.penup()

turtle.listen(xdummy=None, ydummy=None)

while True:
    turtle.onkeypress(turn_Right, "d")
    turtle.onkeypress(turn_Left, "a")
    skane.forward(1)



turtle.mainloop()