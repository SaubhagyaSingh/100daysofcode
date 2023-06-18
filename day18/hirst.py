import turtle as turtle
from turtle import Screen
import random
import colorgram


rgb_colors = []
colors = colorgram.extract("img.jpg", 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(color.rgb)

logo = """

▒█░▒█ ▀█▀ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 　 ▒█▀▀█ ░█▀▀█ ▀█▀ ▒█▄░▒█ ▀▀█▀▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 
▒█▀▀█ ▒█░ ▒█▄▄▀ ░▀▀▀▄▄ ░▒█░░ 　 ▒█▄▄█ ▒█▄▄█ ▒█░ ▒█▒█▒█ ░▒█░░ ▒█░ ▒█▒█▒█ ▒█░▄▄ 
▒█░▒█ ▄█▄ ▒█░▒█ ▒█▄▄▄█ ░▒█░░ 　 ▒█░░░ ▒█░▒█ ▄█▄ ▒█░░▀█ ░▒█░░ ▄█▄ ▒█░░▀█ ▒█▄▄█

\n"""

print(logo)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


speed = [0, 10, 6, 3, 1]

print("Welcome to Hirst Painting Generator\n")
choice = int(
    input(
        "Press 0 for the fastest result\nPress 1 to see the actual process\nPress 2 to see the process a little slower\nPress 3 to see the process slowly\nPress 4 to see the slowest version\n"
    )
)
choice2 = int(input("Enter the size of the dots (Between 15 to 30 preferably)\n"))
t = turtle.Turtle()
turtle.colormode(255)
t.ht()
t.speed(speed[choice])
t.pensize(choice2)

t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)
t.pendown()

for dots in range(1, 100):
    t.dot(20, random.choice(rgb_colors))
    t.penup()
    t.forward(50)
    t.pendown()

    if dots % 10 == 0:
        t.penup()
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
        t.pendown()

screen = Screen()
screen.exitonclick()
