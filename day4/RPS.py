import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = 4
while (choice != 0):
    choice = int(
        input("Enter \n1 for Rock\n2 for Paper\n3 for Scissors\n0 to exit\n"))
    pc_Choice = random.randint(1, 3)

    if (pc_Choice == 1):
        pc_Choice_img = rock
    elif (pc_Choice == 2):
        pc_Choice_img = paper
    else:
        pc_Choice_img = scissors

    if (int(choice) == 1):
        print("You choose Rock: \n")
        print(rock)
    if (int(choice) == 2):
        print("You choose Paper: \n")
        print(paper)
    if (int(choice) == 3):
        print("You choose Scissors: \n")
        print(scissors)

    print("The computer Choose this: ")
    print(pc_Choice_img)

    if (choice == 1 and pc_Choice == 1):
        print("Its a draw.")
    elif (choice == 1 and pc_Choice == 2):
        print("YOU LOSE!")
    elif (choice == 1 and pc_Choice == 3):
        print("You win!")

    if (choice == 2 and pc_Choice == 2):
        print("Its a draw.")
    elif (choice == 2 and pc_Choice == 3):
        print("YOU LOSE!")
    elif (choice == 2 and pc_Choice == 1):
        print("You win!")

    if (choice == 3 and pc_Choice == 3):
        print("Its a draw.")
    elif (choice == 3 and pc_Choice == 1):
        print("YOU LOSE!")
    elif (choice == 3 and pc_Choice == 2):
        print("You win!")
