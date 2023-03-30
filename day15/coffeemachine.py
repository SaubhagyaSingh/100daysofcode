# expresso -- 50ml water 18g coffee
# latte    -- 200ml water 24g coffee 150ml milk
# capuccino-- 250ml water 24g coffee 100ml milk
MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(resources)


def check_aval(type):
    if (MENU[type]["ingredients"]["water"] <= resources["water"] and MENU[type]["ingredients"]["milk"] <= resources["milk"] and MENU[type]["ingredients"]["coffee"] <= resources["coffee"]):
        return 1
    else:
        return 0


x = 1
while x != 0:

    choice = input("What would you like to Order?(expresso/latte/capuccino)")
    if choice == "expresso":
        if check_aval("expresso") == 1:
            cost = int(input("Enter money here..."))
            diff = cost-MENU["expresso"]["cost"]
            if (cost >= MENU["expresso"]["cost"]):
                print("Enjoy your cup of expresso!")
                print(f"Here is your change money {diff}$")
                resources["water"] -= MENU["expresso"]["ingredients"]["water"]
                resources["milk"] -= MENU["expresso"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["expresso"]["ingredients"]["coffee"]

            else:
                print("Not Enough Money!")
        else:
            print("Hardluck:(  ...We ran out of resources")
    elif choice == "latte":
        if check_aval("latte") == 1:
            cost = int(input("Enter money here..."))
            diff = cost-MENU["latte"]["cost"]

            if (cost >= MENU["latte"]["cost"]):
                print(f"Here is your change money {diff}$")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                print("Enjoy your cup of latte!")
            else:
                print("Not Enough Money!")
        else:
            print("Hardluck:(  ...We ran out of resources")
    elif choice == "capuccino":
        if check_aval("capuccino") == 1:
            cost = int(input("Enter money here..."))
            diff = cost-MENU["capuccino"]["cost"]
            if (cost >= MENU["capuccino"]["cost"]):
                print(f"Here is your change money {diff}$")
                resources["water"] -= MENU["capuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["capuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["capuccino"]["ingredients"]["coffee"]
                print("Enjoy your cup of capuccinno!")
            else:
                print("Not Enough Money!")
        else:
            print("Hardluck:(  ...We ran out of resources")
    elif choice == "report":
        report()
    elif choice == "exit":
        x = 0
