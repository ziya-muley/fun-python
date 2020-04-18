import turtle


myTurtle = turtle.Turtle(shape="turtle")
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
purple = (1, 0, 1)
turquiose = (0, 1, 1)
black = (0, 0, 0)

myTurtle.color(red)
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()

myTurtle.color(blue)
myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()

myTurtle.color(purple)
myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()

myTurtle.color(turquiose)
myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()

myTurtle.color(green)
myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()


turtle.exitonclick()