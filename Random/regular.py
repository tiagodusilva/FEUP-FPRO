import turtle

wn = turtle.Screen()

n_sides = int(wn.numinput("Input Window", "How many sides should our polygon have?", 3, minval=3))
length = int(wn.numinput("Input Window", "How long should each side of our polygon be?", 150, minval=0.1))
border_color = wn.textinput("Input Window", "Which color should be the border of the polygon?")
fill_color = wn.textinput("Input Window", "Which color should be the filling of the polygon?")

#n_sides = int(input("Nº of Sides: "))
#length = int(input("Length of Side: "))
#border_color = input("Border color: ")
#fill_color = input("Fill color: ")

angle = 360 / n_sides


poly = turtle.Turtle()
poly.home()
poly.shapesize(0.2, 0.2, 0.2)
poly.color(border_color, fill_color)
poly.pensize(3)

poly.begin_fill()


for _ in range(n_sides):
    poly.forward(length)
    poly.left(angle)

poly.end_fill()

wn.mainloop()
