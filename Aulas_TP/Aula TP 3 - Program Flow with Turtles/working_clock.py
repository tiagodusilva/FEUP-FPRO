import turtle
import datetime


def update_Hours():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute

    hour_angle = ((hours + (minutes / 60)) / 12) * 360

    hour_handle.penup()
    hour_handle.home()
    hour_handle.clear()
    hour_handle.left(90 - hour_angle)
    hour_handle.pendown()
    hour_handle.forward(80)

    turtle.ontimer(update_Hours, 900000)
    return


def update_Minutes():
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = ((minutes + (seconds / 60)) / 60) * 360

    minute_handle.penup()
    minute_handle.home()
    minute_handle.clear()
    minute_handle.left(90 - minute_angle)
    minute_handle.pendown()
    minute_handle.forward(100)

    turtle.ontimer(update_Minutes, 15000)
    return


def update_Seconds():
    now = datetime.datetime.now()

    seconds = now.second

    second_angle = (seconds / 60) * 360

    second_handle.penup()
    second_handle.home()
    second_handle.clear()
    second_handle.left(90 - second_angle)
    second_handle.pendown()
    second_handle.forward(120)

    turtle.ontimer(update_Seconds, 1000)
    return


turtle.setup(500, 500)
wn = turtle.Screen()
#wn.bgcolor("lightgreen")
wn.bgcolor("black")

#Clock Turtle Initializer
clock = turtle.Turtle()
clock.speed(0)
clock.color("blue")
clock.shape("circle")
clock.shapesize(0.5, 0.5, 0.5)
clock.pensize(2)

#Clock Handles Initializer
hour_handle = turtle.Turtle()
hour_handle.hideturtle()
hour_handle.penup()
hour_handle.left(90)
hour_handle.shape("arrow")
hour_handle.pensize(3)
hour_handle.color("darkblue")
hour_handle.speed(0)
#hour_handle._tracer(10)

minute_handle = hour_handle.clone()
minute_handle.pensize(2)
minute_handle.color("lightblue")
#minute_handle._tracer(10)

second_handle = hour_handle.clone()
second_handle.pensize(1)
second_handle.color("blue")
#second_handle._tracer(10)

#Clock Setup
clock.hideturtle()
clock.stamp()
clock.shape("turtle")
clock.shapesize(1, 1, 1)
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

#Time:
update_Hours()
update_Minutes()
update_Seconds()

wn.exitonclick()

turtle.bye()
