
import turtle
import math


def draw_triangle(x=0, y=0, length=100, angle=0, color="white"):
    """
    Draws an equilateral triangle.
    :param color: fill color (default is white)
    :param x: the x-coordinate of the bottom-left corner
    :param y: the y-coordinate of the bottom-left corner
    :param length: the length of each side
    :param angle: the angle that the base makes with the horizontal
    :return:
    """
    brad = turtle.Turtle()
    brad.penup()
    brad.setx(x)
    brad.sety(y)
    brad.pendown()
    brad.hideturtle()
    brad.color(color)
    brad.fill(True)
    brad.left(angle)
    brad.forward(length)
    brad.left(120)
    brad.forward(length)
    brad.left(120)
    brad.forward(length)
    brad.fill(False)


def divide_triangle(x, y, length, color="Black"):
    """
    Draws a triangle inside the triangle with bottom-left
    position given by the coordinates
    :param x: the x-coordinate of the bottom-left corner of the original triangle
    :param y: the y-coordinate of the bottom-left corner of the original triangle
    :param length: the side-length of the original triangle
    :return: a list of tuples -- one for each triangle -- each one is
    the (x, y, length) as required for another iteration of this function.
    """
    draw_triangle(x=x + length / 2, y=y, length=length / 2, angle=60, color=color)
    return [(x, y, length / 2),
            (x + length / 2, y, length / 2),
            (x + length / 4, y + length * math.sqrt(3) / 4, length / 2)]


def draw_sierpinski_triangle():
    window = turtle.Screen()
    max_length = 400
    window.bgcolor("#aa44ee")
    draw_triangle(-max_length / 2, -max_length / 2, max_length)
    current_triangles = [(-max_length / 2, -max_length / 2, max_length)]
    while len(current_triangles) < 100:
        next_triangles = []
        for x, y, length in current_triangles:
            next_triangles += divide_triangle(x, y, length, color="#aa44ee")
        current_triangles = next_triangles
    window.exitonclick()


draw_sierpinski_triangle()


