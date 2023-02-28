
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1 = name1.lower()
n2 = name2.lower()
x = n1.count("t")+n2.count("t")
x = x+n1.count("r")+n2.count("r")
x = x+n1.count("u")+n2.count("u")
x = x+n1.count("e")+n2.count("e")

y = n1.count("l")+n2.count("l")
y = y+n1.count("o")+n2.count("o")
y = y+n1.count("v")+n2.count("v")
y = y+n1.count("e")+n2.count("e")

z = x*10+y

if (z < 10 or z > 90):
    print(f"Your score is {z}, you go together like coke and mentos.")
elif (z <= 50 and z >= 40):
    print(f"Your score is {z}, you are alright together.")
else:
    print(f"Your score is {z}")
