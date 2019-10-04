import turtle

def move_Left():
    turtle_x = rangel.pos()[0] - 8
    rangel.setx(turtle_x)
    return

def move_Right():
    turtle_x = rangel.pos()[0] + 8
    rangel.setx(turtle_x)
    return

def fire(x, y):
    if shot_1.pos()[1] < turtle_Height:
        shot_1.setpos(rangel.pos()[0], turtle_Height + 20)
        shot_1.showturtle()
    elif shot_2.pos()[1] < turtle_Height:
        shot_2.setpos(rangel.pos()[0], turtle_Height + 20)
        shot_2.showturtle()
    elif shot_3.pos()[1] < turtle_Height:
        shot_3.setpos(rangel.pos()[0], turtle_Height + 20)
        shot_3.showturtle()
    elif shot_4.pos()[1] < turtle_Height:
        shot_4.setpos(rangel.pos()[0], turtle_Height + 20)
        shot_4.showturtle()
    return

def shot_Movement_Cycle():
    shot_pos_y = shot_1.pos()[1]
    if shot_pos_y <= s_top and shot_pos_y >= turtle_Height:
        shot_1.sety(shot_pos_y + 20)
    else: 
        shot_1.hideturtle()

    shot_pos_y = shot_2.pos()[1]
    if shot_pos_y <= s_top and shot_pos_y >= turtle_Height:
        shot_2.sety(shot_pos_y + 20)
    else:
         shot_2.hideturtle()
    
    shot_pos_y = shot_3.pos()[1]
    if shot_pos_y <= s_top and shot_pos_y >= turtle_Height:
        shot_3.sety(shot_pos_y + 20)
    else:
         shot_3.hideturtle()
         
    shot_pos_y = shot_4.pos()[1]
    if shot_pos_y <= s_top and shot_pos_y >= turtle_Height:
        shot_4.sety(shot_pos_y + 20)
    else:
         shot_4.hideturtle()

    wn.ontimer(shot_Movement_Cycle, 50)
    return

turtle.setup(920, 600)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Shooters")

s_height = wn.screensize()[0]
s_width = wn.screensize()[1]
s_top = 300

#Setup Rangel
rangel = turtle.Turtle()
rangel.color("lightgreen")
rangel.fillcolor("darkgreen")
rangel.penup()
rangel.shape("turtle")
rangel.shapesize(1.5,1.5,1.5)
rangel.left(90)
turtle_Height = -s_height/1.5
rangel.sety(turtle_Height)

#Setup all the projectiles
shot_1 = turtle.Turtle()
shot_1.hideturtle()
shot_1.shape("arrow")
shot_1.shapesize(.4,1,1)
shot_1.color("darkred")
shot_1.fillcolor("red")
shot_1.penup()
shot_1.speed(0)
shot_1.left(90)
shot_1.setpos(0, -800)

shot_2 = shot_1.clone()
shot_3 = shot_1.clone()
shot_4 = shot_1.clone()

shot_Movement_Cycle()

turtle.listen(xdummy=None, ydummy=None)
turtle.onkeypress(move_Right, "d")
turtle.onkeypress(move_Left, "a")
wn.onclick(fire, btn=1)


turtle.mainloop()