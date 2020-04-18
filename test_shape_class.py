import turtle

t = turtle.Turtle(shape="turtle")
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
purple = (1, 0, 1)
turquiose = (0, 1, 1)
black = (0, 0, 0)

class Rectangle:
    def __init__(self, x, y, length, width):
        self.length = length
        self.width = width
        self.x = x
        self.y = y

    def draw(self):
        turtle.setposition(self.x, self.y)

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getLocation(self):
        return (self.x, self.y)

    def getColor(self):
        pass


class Circle:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self):
        pass

    def getRadius():
        pass

    def getLocation(self):
        pass

    def getColor(self):
        pass    

shapeRectangle = Rectangle(x=0, y=0, length=10, width=15)
shapeRectangle.draw()
shapeCircle = Circle(x=0, y=0, radius=10)
shapeCircle.draw()

turtle.exitonclick()