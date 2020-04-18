import turtle

t = turtle.Turtle(shape="turtle")
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
purple = (1, 0, 1)
turquiose = (0, 1, 1)
black = (0 ,0, 0)

class Mouse:
    def _draw_circle(self, x, y, radius, color):
        t.color(color)
        t.penup()
        t.setposition(x,y)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    def draw(self, x, y):
        pass  
    

class MickeyMouse(Mouse):
    def _draw_head(self):
        self._draw_circle(x=0+self.x_offset, y=0+self.y_offset, radius=100, color=black)

    def _draw_left_ear(self):
        self._draw_circle(-100+self.x_offset, 100+self.y_offset, 90, black)

    def _draw_right_ear(self):
        self._draw_circle(100+self.x_offset, 100+self.y_offset, 90, black)

    def draw(self, x, y):
        self._draw_head()
        self._draw_left_ear()
        self._draw_right_ear()

class MinnieMouse(Mouse):
    def _draw_head(self, x, y):
        self._draw_circle(
                x = 0 + self.x_offset,
                y = 0 + self.y_offset,
                radius=100,
                color=black)

    def _draw_left_ear(self, x, y):
        self._draw_circle(
                x = - 100 + self.x_offset,
                y = 100 + self.y_offset,
                radius=90,
                color=black)

    def _draw_right_ear(self):
        self._draw_circle(100 + self.x_offset, 100 + self.y_offset, 90, black)
        
    def _draw_bow(self):
        #right_of_bow
        self._draw_circle(75 + self.x_offset, 170 + self.y_offset, 50, turquiose)

        #left_of_bow
        self._draw_circle(-75 + self.x_offset, 170 + self.y_offset, 50, turquiose)

        #blue_bow
        self._draw_circle(0 + self.x_offset, 170 + self.y_offset, 30, blue)

    def draw(self, x, y):
        self._draw_head(x, y)
        self._draw_left_ear(x, y)
        self._draw_right_ear(x, y)
        self._draw_bow(x, y)

micky = MickeyMouse()
micky.draw(0, -300)

minnie = MinnieMouse()
minnie.draw(0, 300)

t.penup()
t.setposition(180, 500)

turtle.exitonclick()