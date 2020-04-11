import turtle

t = turtle.Turtle(shape="turtle")
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
purple = (1, 0, 1)
turquiose = (0, 1, 1)
black = (0 ,0, 0)

def draw_circle(x, y, radius, color):
    t.color(color)
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_micky_mouse():
     # head
    draw_circle(x=0, y=0, radius=100, color=black)
    # ear 1
    draw_circle(-100, 100, 90, black)
    #ear 2
    draw_circle(100, 100, 90, black)

draw_micky_mouse()

turtle.exitonclick()