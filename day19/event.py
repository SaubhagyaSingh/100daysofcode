from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def square():
    t.shape("arrow")
    t.color("red")
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(360)


screen.listen()
screen.onkey(key="space", fun=square)
screen.exitonclick()
