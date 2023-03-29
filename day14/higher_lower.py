import random
logo = """
  ______                                                _
 |  ____|                                              | |
 | |__ __ _ _ __ ___   ___   _ __   __ _ _ __ ___   ___| |
 |  __/ _` | '_ ` _ \ / _ \ | '_ \ / _` | '_ ` _ \ / _ \ |
 | | | (_| | | | | | |  __/ | | | | (_| | | | | | |  __/_|
 |_|  \__,_|_| |_| |_|\___| |_| |_|\__,_|_| |_| |_|\___(_)

                                                          """
sports_players = {
    "Ronaldo": 567_000_000, "Messi": 448_000_000, "The Rock": 371_000_000, "virat kohli": 242_000_000, "Neymar": 206_000_000, "LeBron James": 149_000_000, "Mbappe": 101_000_000, "Magnus carlsun": 1_000_000, "MS Dhoni": 41_000_000, "Sunil chetri": 4_300_000
}
celebs = {
    "Selena Gomez": 405_000_000, "Kylie Jenner": 383_000_000, "Ariana grande": 362_000_000, "kim kardashian": 350_000_000, "Beyonce": 302_000_000, "Justin Beiber": 283_000_000, "Taylor Swift": 251_000_000, "Jennifer Lopez": 239_000_000, "Nicki minaj": 214_000_000, "Katy Perry": 194_000_000
}


print(logo)
x = 1
while (x == 1):
    print("Welcome to Fame game!\nGuess which celebrity or sports player has more instagram followers.\nScore full for a surprise! ")
    score = 0
    round = 0
    while round < 5:
        round += 1
        player_name = random.choice(list(sports_players))
        celeb_name = random.choice(list(celebs))

        pf = sports_players[player_name]
        cf = celebs[celeb_name]
        choice = int(input(
            f"Who Do you think has more followers\n {player_name} or {celeb_name}\nPress 1 for {player_name}\nPress 2 for {celeb_name}"))
        if pf > cf and choice == 1:
            print(
                f"Correct Answer! {player_name} has {pf} followers where as {celeb_name} has only {cf}\n")
            score += 1
        elif pf > cf and choice == 2:
            print(
                f"Wrong Answer! {player_name} has {pf} followers where as {celeb_name} has only {cf}\n")
        elif pf < cf and choice == 2:
            print(
                f"Correct Answer! {celeb_name} has {cf} followers where as {player_name} has only {pf}\n")
            score += 1
        elif pf < cf and choice == 1:
            print(
                f"Wrong Answer! {celeb_name} has {cf} followers where as {player_name} has only {pf}\n")
    print(f"Your final score is: {score}")
    x = int(input("Enter 1 to play again\nEnter 0 to quit\n"))
