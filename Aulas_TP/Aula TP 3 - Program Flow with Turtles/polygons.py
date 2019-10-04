import turtle

wn = turtle.Screen()

length = 50
poly = turtle.Turtle()
poly.speed(0)
poly.shapesize(0.01, 0.01, 0.01)

n_sides = 3
angle = 360 / n_sides
for _ in range(n_sides):
    poly.forward(length)
    poly.left(angle)

n_sides = 4
angle = int(360 / n_sides)
for _ in range(n_sides):
    poly.forward(length)
    poly.left(angle)

n_sides = 6
angle = int(360 / n_sides)
for _ in range(n_sides):
    poly.forward(length)
    poly.left(angle)

n_sides = 8
angle = int(360 / n_sides)
for _ in range(n_sides):
    poly.forward(length)
    poly.left(angle)

wn.mainloop()
