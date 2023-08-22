import turtle
from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("crimson")

# # Draw Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# # Draw dashed line
# timmy.left(45)
# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# # Draw many shapes in different colors
# colors = ["deep sky blue", "orchid", "dark orange", "lime", "spring green", "medium turquoise", "red", "dodger blue"]
# for i in range(3, 11):
#     angle = 360/i
#     color = random.choice(colors)
#     timmy.color(color)
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(angle)


# # Random walk
# turtle.colormode(255)
# directions = [0, 90, 180, 270]
# timmy.speed("fast")
# timmy.pensize(10)
# steps = random.randint(50, 80)
#
#
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     rgb = (r, g, b)
#     return rgb
#
#
# for _ in range(steps):
#     color = rand_color()
#     direction = random.choice(directions)
#
#     timmy.color(color)
#     timmy.left(direction)
#     timmy.forward(30)


# # Spirograph
# turtle.colormode(255)
# timmy.pensize(2)
# timmy.speed("fastest")
#
#
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     rgb = (r, g, b)
#     return rgb
#
#
# angle = 5
# circles = int(360/angle)
#
# for i in range(circles):
#     timmy.color(rand_color())
#     timmy.circle(100)
#     timmy.left(angle)
#


# Dot painting
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

colors = colorgram.extract("image.jpeg", 10)
rgb_colors = []
offset = 225
num_of_dots = 10
space_between = 50

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)


for y in range(num_of_dots):
    for x in range(num_of_dots):
        timmy.setpos(x * space_between - offset, y * space_between - offset)
        timmy.dot(20, random.choice(rgb_colors))


screen = Screen()
screen.exitonclick()
