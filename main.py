from turtle import Turtle, Screen

Bob = Turtle()
screen = Screen()


def move_forward():
    Bob.fd(10)


def move_backward():
    Bob.bk(10)


def rotate_left():
    Bob.lt(10)


def rotate_right():
    Bob.rt(10)


def clear():
    Bob.penup()
    Bob.home()
    Bob.clear()
    Bob.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
