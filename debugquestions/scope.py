# q1 scope
# base_salary = 80000


# def promotion():
#     base_salary += 20000
#     print(f"Your current salary after promotion: {base_salary}")


# promotion()

# Q2 lists

# enemies = ["Zombies", "Aliens", "Predators"]

# enemy_type = 3
# current_threat = enemies[enemy_type]
# print(f"Beware there are {current_threat} outside the safe zone!")

# Q3    Diff data types


# bill = float(input("What was the total bill?\n"))
# n = input("How many people to split the bill?\n")

# pay = (bill/n)
# print(f"Each person should pay: {pay}")

# Q4 indentation:

# def paint_calc(height, width, cover):
#     cans = (height*width)/cover
#     if (cans % 2 != 0):
#         cans = cans+1
#         print(f"You'll need {int(cans)} cans of paint.")


# test_h = 10
# test_w = 22
# coverage = 5
# cover = 4
# paint_calc(height=test_h,  cover=coverage, width=test_w)

# Q5    and or
# def prime_checker(number):
#     x = 1
#     k = -2
#     while (x < number):
#         if (number % x == 0 && x < 1):
#             k += 1
#         x += 1
#     if (k >= 1):
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

# Q6 fstring
# print("Welcome to the Sports team name generator")
# city = input("Enter the city you grew up in\n")
# cool = input("Enter a cool thing\n")
# print("Your band name is (city) " + cool)

# q7 elif
# def buying_candy(amount_of_money):
#     if amount_of_money < 2:
#         return 1
#     else if (amount_of_money > 2):
#         return 0


# if (buying_candy(4) = 0):
#     print("Sufficient money to buy candy")

# q8    assign ,or and compare operators.

# number == 14
# i == 2
# x == 0
# while i < number:
#     if (i % 2=0) | | (i % 4=0):
#         x = x+1
#     i += 1
# print(f"the total numbers divisible by 2 or 4 are: {x}")

# q9
# ages = {
#     'pam'= 24,
#     'jim'= 22,
#     'michael'= 43,
# }
# print(f'Michael is {ages["michael"]} years old.')

# q10
# num = 15
# if num >= 0:
#  if num == 0:
#     print("Zero")
#  else:
#     print("Positive number")
#  else:
#     print("Negative number")
