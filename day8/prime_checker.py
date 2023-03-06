
def prime_checker(number):
    x = 1
    k = -2
    while (x < number):
        if (number % x == 0):
            k += 1
        x += 1
    if (k >= 1):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
