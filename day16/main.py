import prettytable as pt
import turtle as tl
saubhi = tl.Turtle()
my_screen = tl.Screen()
# print(my_screen.canvheight)
saubhi.shape("turtle")
saubhi.color("coral")
saubhi.forward(100)
# my_screen.exitonclick()
x = pt.PrettyTable()
x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Pokemon Name", ["Electric", "Water", "Fire"])
x.align = 'l'
print(x)
