from turtle import Turtle, Screen
import random

## Etch-A-Sketch
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_clockwise():
#     tim.right(10)
#
#
# def turn_ccwise():
#     tim.left(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forward, "f")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(turn_ccwise, "a")
# screen.onkey(clear, "c")
# screen.exitonclick()


# Turtle Race

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You win. {winning_color} won!")
            else:
                print(f"You lose. {winning_color} won!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
