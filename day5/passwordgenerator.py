import random
print("Welcome to the Password Generator")
l = int(input("Enter the Number of charecters you want in your password\n"))
s = int(input("Enter the number of symbols you want in your password\n"))
n = int(input("Enter the total numbers you want in your password\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
finalpasswd = ""
for char in range(1, l+1):
    password += random.choice(letters)

for sym in range(1, s+1):
    password += random.choice(symbols)

for char in range(1, n+1):
    password += random.choice(numbers)

for i in range(0, len(password)+1):
    finalpasswd += random.choice(password)
# could also be done with random.shuffle
print(finalpasswd)
