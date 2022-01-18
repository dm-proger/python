import turtle

class Shape():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw_shape(self):
        raise NotImplementedError("Subclass must be implement abstract method")


class Circle(Shape):
    def draw_shape(self):
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.down()
        turtle.circle(self.radius)
        turtle.up()


class Square(Shape):
    def draw_shape(self):
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.down()
        turtle.forward(self.radius * 2)
        turtle.right(90)
        turtle.forward(self.radius * 2)
        turtle.right(90)
        turtle.forward(self.radius * 2)
        turtle.right(90)
        turtle.forward(self.radius * 2)
        turtle.right(90)
        turtle.up()


my_square = Square(0, 0, 25)
my_circle = Circle(25, 25, 25)
my_square.draw_shape()
my_circle.draw_shape()
turtle.done()
