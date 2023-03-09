from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def maxbidder(bid_rec):
    highest_bid = 0
    for bidder in bid_rec:
        bid_amount = bid_rec[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of {highest_bid}")


bids = {}
bid_End = False
while bid_End != True:
    name = input("Enter your name: ")
    price = int(input("Enter your bidding price: "))
    bids[name] = price
    should_continue = input("Are there any more bidders?Type y or n : ")
    if (should_continue == 'n'):
        bid_End = True
        maxbidder(bids)
    elif (should_continue == 'y'):
        clear()
