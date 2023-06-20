from turtle import Turtle, Screen, write
import random


logo = """

████████╗██╗░░░██╗██████╗░████████╗██╗░░░░░███████╗  ██████╗░░█████╗░░█████╗░███████╗
╚══██╔══╝██║░░░██║██╔══██╗╚══██╔══╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
░░░██║░░░██║░░░██║██████╔╝░░░██║░░░██║░░░░░█████╗░░  ██████╔╝███████║██║░░╚═╝█████╗░░
░░░██║░░░██║░░░██║██╔══██╗░░░██║░░░██║░░░░░██╔══╝░░  ██╔══██╗██╔══██║██║░░██╗██╔══╝░░
░░░██║░░░╚██████╔╝██║░░██║░░░██║░░░███████╗███████╗  ██║░░██║██║░░██║╚█████╔╝███████╗
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝
"""

screen = Screen()
screen.bgcolor("black")

logowriter = Turtle()
logowriter.ht()
logowriter.goto(-350, 200)
logowriter.color("red")
logowriter.write(logo)

finishline = Turtle()

finishline.ht()
finishline.goto(270, -150)
finishline.color("white")
finishline.pensize(5)
finishline.setheading(90)
finishline.forward(300)

speed = []

for i in range(5):
    s = random.randint(1, 10)
    speed.append(s)


t1 = Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-300, -100)
t1.speed(speed[0])
t1.forward(40)

t2 = Turtle()
t2.shape("turtle")
t2.color("pink")
t2.penup()
t2.goto(-300, -50)
t2.speed(speed[1])
t2.forward(40)


t3 = Turtle()
t3.shape("turtle")
t3.color("purple")
t3.penup()
t3.goto(-300, 0)
t3.speed(speed[2])
t3.forward(40)


t4 = Turtle()
t4.shape("turtle")
t4.color("yellow")
t4.penup()
t4.goto(-300, 50)
t4.speed(speed[3])
t4.forward(40)


t5 = Turtle()
t5.shape("turtle")
t5.color("orange")
t5.penup()
t5.goto(-300, 100)
t5.speed(speed[4])
t5.forward(40)

screen2 = Screen()
answer = screen2.textinput(
    "", "Welcome to The Turtle race!Pick a color to bet on a turtle"
)

k = 0
all_turtles = [t1, t2, t3, t4, t5]

while k != 1:
    for turtle in all_turtles:
        if turtle.xcor() >= 250:
            winner = turtle.color()
            k = 1
            break
        if k != 1:
            random_dist = random.randint(0, 10)
            turtle.forward(random_dist * turtle.speed())

print(f"The race was won by {winner[0]}")
if (winner[0] == answer) or (winner[0] == answer.lower()):
    print("You Guessed it right!Good Job.")
else:
    print("You lost!")

screen.exitonclick()
