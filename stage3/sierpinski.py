import turtle
import math
import time


def draw_square(angle=10):
    brad = turtle.Turtle()
    brad.color("#008822")
    brad.shape("turtle")
    brad.right(angle)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)


def draw_circle():
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("arrow")
    brad.circle(100)


def draw_triangle(first_angle=60, second_angle=60):
    sine_first = math.sin(first_angle * math.pi / 180)
    sine_second = math.sin(second_angle * math.pi / 180)
    sine_third = math.sin((180 - first_angle - second_angle) * math.pi / 180)
    second_side = 100 * sine_third / sine_second
    third_side = 100 * sine_first / sine_second
    brad = turtle.Turtle()
    brad.forward(100)
    brad.left(180 - first_angle)
    brad.forward(second_side)
    brad.left(180 - second_angle)
    brad.forward(third_side)
    brad.left(first_angle + second_angle)


def draw_equilateral(x=0, y=0, length=100, angle=0, color="white"):
    """
    Draws an equilateral triangle.
    :param color: fill color (default is white)
    :param x: the x-coordinate of the bottom-left corner
    :param y: the y-coordinate of the bottom-left corner
    :param length: the length of each side
    :param angle: the angle that the base makes with the horizontal
    :return:
    """
    start = time.time()
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


def divide_equilateral(x, y, length, color="Black"):
    """
    Draws a triangle inside the triangle with bottom-left
    position given by the coordinates
    :param x: the x-coordinate of the bottom-left corner of the original triangle
    :param y: the y-coordinate of the bottom-left corner of the original triangle
    :param length: the side-length of the original triangle
    :return:
    """
    draw_equilateral(x=x + length / 2, y=y, length=length / 2, angle=60, color=color)
    return [(x, y, length / 2),
            (x + length / 2, y, length / 2),
            (x + length / 4, y + length * math.sqrt(3) / 4, length / 2)]


def draw_art():
    window = turtle.Screen()
    max_length = 400
    window.bgcolor("#aa44ee")
    TRIANGLE_COLOR = "#aa44ee"
    # draw first triangle
    draw_equilateral(-max_length / 2, -max_length / 2, max_length)
    # divide it
    current_triangles = [(-max_length / 2, -max_length / 2, max_length)]
    while len(current_triangles) < 100:
        next_triangles = []
        for x, y, length in current_triangles:
            next_triangles += divide_equilateral(x, y, length, color=TRIANGLE_COLOR)
        current_triangles = next_triangles
    window.exitonclick()


draw_art()

