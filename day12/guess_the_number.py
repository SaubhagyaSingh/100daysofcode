import random
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

title = '''________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________  ________      
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \|\_____  \     
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \|____|\  \    
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\    \ \__\   
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \|    \|__|   
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\        ___ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|      |\__\
                                 \|_________\|_________|                                                                                                                       \|__|
                                                                                                                                                                                    
                                                                                                                                                                                    '''
print(title)
flag = 0


def guesstime(x):
    n = random.randint(1, 100)
    print(f"You have {x} chances to guess the number correctly")
    chances = 0
    while chances < x:

        guess = int(input("Enter your first guess"))
        diff = n-guess
        if n == guess:
            print(
                f"Correct the number was {n} you guessed the number in {chances+1} turns")
            break
        elif (diff > 15 and diff < 30):
            print("Try again your guess was high")
        elif (diff > 15 and diff < 100):
            print("Try again your guess too was high")
        elif (diff < 15 and diff < 30):
            print("Try again your guess was low")
        elif (diff < 15 and diff < 100):
            print("Try again your guess too was too low")
        chances += 1


while flag == 0:
    choice1 = int(input(
        "Welcome to guess the number game!\n1 to play on easy mode\n2 for medium difficulty\n3 for hard difficulty\n"))

    if choice1 == 1:
        guesstime(10)
    elif choice1 == 2:
        guesstime(7)
    elif choice1 == 3:
        guesstime(5)
    choice2 = int(
        input("Press 0 to play again\n Press any other number to quit"))
    flag = choice2
