from art import logo
print(logo)

# add


def add(n1, n2):
    return (n1+n2)
# substract


def substract(n1, n2):
    return (n1-n2)
# multiply


def multiply(n1, n2):
    return (n1*n2)

# divide


def divide(n1, n2):
    return (n1/n2)


# main
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# driver code inside the calculator function


def calculator():
    num1 = float(input("Enter the first Number: "))
    for symbols in operations:
        print(symbols)
        print(" ")
    operation_symbol = input("Enter the operation you want to perform: ")
    num2 = int(input("Enter the second number: "))

    # An alternate aproach to this could be:
    # if operation_symbol == list(operations.keys())[0]:
    #     result = add(num1, num2)
    # elif operation_symbol == list(operations.keys())[1]:
    #     result = substract(num1, num2)
    # elif operation_symbol == list(operations.keys())[2]:
    #     result = multiply(num1, num2)
    # if operation_symbol == list(operations.keys())[3]:
    #     result = divide(num1, num2)

    calc_func = operations[operation_symbol]
    result = calc_func(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    should_continue = 'y'
    while should_continue != 'n':
        should_continue = input(
            "Enter y to continue...\nEnter n to enter new values\nEnter exit to exit the program: ")
        if (should_continue == 'y'):
            num1 = result
        elif (str(should_continue) == "exit"):
            break
        elif (should_continue == 'n'):
            calculator()
            break
        for symbols in operations:
            print(symbols)
            print(" ")
        operation_symbol = input("Enter the operation you want to perform: ")
        num2 = float(input("Enter the second number: "))
        calc_func = operations[operation_symbol]
        result = calc_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")


# main
calculator()
