import random
# wordlist
wordlist = ['india', 'canada', 'japan']
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
g = 0
word = random.choice(wordlist)
x = len(word)
chosen_letter = [" _ "]*x
print(chosen_letter)
z = 0
k = 0
while z < 7 and x != g:
    lul = 2

    guess = input("Guess a letter: ").lower()
    i = -1
    for letter in word:
        i = i+1
        if (g == x):
            break
        elif (guess == letter):
            chosen_letter[i] = [guess]
            lul = 0
            g += 1
        elif (i == x-1 and guess != letter and lul != 0):
            z += 1
            i = -1
            print(HANGMANPICS[k])
            k += 1
    if (g == x):
        print("YOU WIN!")
    print(chosen_letter)

if (z >= 7):
    print("YOU LOSE!")
