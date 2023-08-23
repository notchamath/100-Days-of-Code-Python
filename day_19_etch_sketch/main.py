from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_ccwise():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backwards, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_ccwise, "a")
screen.onkey(clear, "c")

screen.exitonclick()