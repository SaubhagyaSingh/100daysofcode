import turtle as turtle
from turtle import Screen
import random


logo = """

░██████╗██████╗░██╗██████╗░░█████╗░░██████╗░██████╗░░█████╗░██████╗░██╗░░██╗
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░██████╔╝██║██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██████╔╝███████║
░╚═══██╗██╔═══╝░██║██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██╔═══╝░██╔══██║
██████╔╝██║░░░░░██║██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░░░░░██║░░██║
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝"""

print(logo)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


speed = [0, 10, 6, 3, 1]

print("Welcome to Spirograph Generator\n")
choice = int(
    input(
        "Press 0 for the fastest result\nPress 1 to see the actual process\nPress 2 to see the process a little slower\nPress 3 to see the process slowly\nPress 4 to see the slowest version\n"
    )
)
choice2 = int(input("Enter the size of the pen (Between 0 to 5 preferably)\n"))
t = turtle.Turtle()
turtle.colormode(255)


for i in range(0, 60):
    t.speed(speed[choice])
    t.pensize(choice2)
    t.setheading(i * 6)
    cur_color = random_color()
    t.color(cur_color)
    t.circle(100)


screen = Screen()
screen.exitonclick()
