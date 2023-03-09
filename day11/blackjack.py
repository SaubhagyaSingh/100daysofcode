import random
from art import logo
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

print(logo)


def sum(hand):
    total = 0
    for value in hand:
        total += value
    if (total > 21):
        return 1
    else:
        return 0


def totalvalue(hand):
    total = 0
    for value in hand:
        total += value
    return total


deck = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
        "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
keys = list(deck.keys())
random_key1 = random.choice(keys)
random_key2 = random.choice(keys)
random_key3 = random.choice(keys)
random_key4 = random.choice(keys)

gg = 0
myhand = [deck[random_key1], deck[random_key2]]
dealer_hand = [deck[random_key3], deck[random_key4]]
print(f"My Cards: \n{myhand}")
print(f"Dealer's Cards: \n{dealer_hand[0]}")
chance = 0
while gg != 1:

    choice = int(
        input("Enter 1 to get a card\nEnter 2 to pass\nEnter 3 to exit: "))
    if choice == 1:
        chance += 1
        random_key5 = random.choice(keys)
        myhand.append(deck[random_key5])
        gg = sum(myhand)
        if (gg == 1):
            print(f"Total value of my hand: {totalvalue(myhand)}")
            print(f"Total value of dealer's hand: {totalvalue(dealer_hand)}")
            print("YOU LOST ")
        elif (gg == 0):
            print(f"My Cards:\n{myhand}")
        random_key6 = random.choice(keys)
        dealer_hand.append(deck[random_key6])
        gg = sum(dealer_hand)
        if (gg == 1):
            print(f"Total value of my hand: {totalvalue(myhand)}")
            print(f"Total value of dealer's hand: {totalvalue(dealer_hand)}")
            print("YOU WON! ")
        elif (gg == 0):
            print(f"Dealer's new card: \n{dealer_hand[chance]}")
    elif choice == 2:
        mytotal = totalvalue(myhand)
        dealers_total = totalvalue(dealer_hand)
        print(f"My total: {mytotal}")
        print(f"Dealer's total: {dealers_total}")
        for i in range(0, chance+1):

            if (myhand[i] == 1):
                myhand.insert(i, 11)
            if (dealer_hand[i] == 1):
                dealer_hand.insert(i, 11)
        if (mytotal > dealers_total):
            print("You win")
        elif (mytotal < dealers_total):
            print("YOU LOSE!")
        elif (mytotal == dealers_total):
            print("Its a DRAW")
    elif choice == 3:
        gg = 1
