from random import choice
ai = choice(["rock", "paper", "scissors"])

print("...rock...")
print("...paper...")
print("...scissors...")
player = input("Choose a sign: ").lower()
print("Go!")

if player:
    if player == ai:
        print("{} vs {} - Draw!".format(player.capitalize(), ai.capitalize()))
    elif player == "rock":
        if ai == "paper":
            print("Rock vs Paper - you lost :(")
        elif ai == "scissors":
            print("Rock vs Scissors - you won!")
    elif player == "paper":
        if ai == "rock":
            print("Paper vs Rock - you won!")
        elif ai == "scissors":
            print("Paper vs Scissors - you lost :(")
    elif player == "scissors":
        if ai == "rock":
            print("Scissors vs Rock - you lost :(")
        elif ai == "paper":
            print("Scissors vs Paper - you won!")
else:
    print("You need to make a choice!")
