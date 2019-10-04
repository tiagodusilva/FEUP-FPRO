import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.tracer(10000, 0)

star = turtle.Turtle()
star.speed(0)
star.color("white")
star.shape("circle")
star.shapesize(1.2, 1.2, 1.2)
star.pensize(5)

n_points = int(wn.numinput("Input Window", "How many points should our star have?"))

star.left(90)
star.home()
angle = 360 / n_points
for _ in range(n_points):
    star.left(angle)
    star.forward(200)
    star.stamp()
    star.backward(200)

wn.update()

wn.mainloop()
