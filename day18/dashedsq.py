from turtle import Turtle, Screen

t = Turtle()

for i in range(20):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


sc = Screen()
sc.exitonclick()
