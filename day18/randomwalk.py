import turtle as turtle
from turtle import Screen
import random

colors = [
    "red",
    "blue",
    "pink",
    "black",
    "green",
    "yellow",
    "purple",
    "wheat",
    "orange",
    "SlateGray",
    "IndianRed",
]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


d = [0, 90, 180, 270]

logo = """

██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░░███╗  ░██╗░░░░░░░██╗░█████╗░██╗░░░░░██╗░░██╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░████║  ░██║░░██╗░░██║██╔══██╗██║░░░░░██║░██╔╝
██████╔╝███████║██╔██╗██║██║░░██║██║░░██║██╔████╔██║  ░╚██╗████╗██╔╝███████║██║░░░░░█████═╝░
██╔══██╗██╔══██║██║╚████║██║░░██║██║░░██║██║╚██╔╝██║  ░░████╔═████║░██╔══██║██║░░░░░██╔═██╗░
██║░░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░╚═╝░██║  ░░╚██╔╝░╚██╔╝░██║░░██║███████╗██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""
print(logo)
print("Welcome to Random Walk Generator\n")
choice = int(
    input(
        "Press 0 for the fastest result\nPress 1 to see the actual process\nPress 2 to see the process a little slower\nPress 3 to see the process slowly\nPress 4 to see the slowest version\n"
    )
)

choice2 = int(
    input("Press 0 for Artstyle 1(limited Colors)\nPress 1 for Artstyle 2(All colors)")
)

t = turtle.Turtle()
turtle.colormode(255)

speed = [0, 10, 6, 3, 1]
for i in range(200):
    t.speed(speed[choice])
    t.pensize(7)
    t.forward(30)
    t.setheading(random.choice(d))
    if choice2 == 0:
        t.color(random.choice(colors))
    elif choice2 == 1:
        cur_color = random_color()
        t.color(cur_color)

screen = Screen()
screen.exitonclick()
