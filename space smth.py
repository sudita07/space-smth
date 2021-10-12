import turtle
import os
sun=turtle.Screen()
sun.bgcolor("orange")
border=turtle.Turtle()
border.shape("triangle")
border.color("green")

border.penup()
border.setposition(-200,-200)
border.pendown()
border.pensize(4)
for side in range(4):
    border.forward(400)
    border.left(90)
border.hideturtle()
queen=turtle.Turtle()
queen.color("blue")
queen.shape("circle")
queen.penup()
queen.setposition(0,-190)
queenspeed=12

king=turtle.Turtle()
king.color("red")
king.shape("turtle")
king.penup()
king.setposition(0,180)
king.setheading(270)
kingspeed=5
def down():
    x=queen.ycor()
    x-=queenspeed
    if x<-200:
        x=-200
    queen.sety(x)
def up():
    n=queen.ycor()
    n+=queenspeed
    if n>200:
        n=200
    queen.sety(n)
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.listen()


while True:
    x=king.xcor()
    x+=kingspeed
    king.setx(x)
    if king.xcor()>200:
        y=king.ycor()
        y-=20
        kingspeed*=-1
        king.sety(y)
    if king.xcor()<-200:
        y=king.ycor()
        y-=20
        kingspeed*=-1
        king.sety(y)

    sun.update()