# Tip Calculator
print("Welcome to the tip calculator\n")
bill = float(input("What was the total bill?\n"))
n = float(input("How many people to split the bill?\n"))
p = float(input("enter the percentage of tip\n"))
pay = float((bill/n)*(p/10))
print(f"Each person should pay: {pay}")
