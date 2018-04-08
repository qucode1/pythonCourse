from random import choice
player_wins = 0
computer_wins = 0
winning_score = 2
# doen't work - uses the initial values of computer_wins and player_wins
# scores = "\nScores: {} - {}".format(player_wins, computer_wins)

while player_wins < winning_score and computer_wins < winning_score or computer_wins == player_wins:
    ai = choice(["rock", "paper", "scissors"])

    print("\nrock, paper, scissors...")
    # print("...paper...")
    # print("...scissors...")
    player = input("Choose a sign: ").lower()
    if player == "quit" or player == "q":
        break
    print("Go!\n")

    if player:
        if player == ai:
            computer_wins += 1
            player_wins += 1
            print("{} vs {} - Draw!".format(
                player.capitalize(), ai.capitalize()
            ) + "\nScores: {} - {}".format(player_wins, computer_wins))
        elif player == "rock":
            if ai == "paper":
                computer_wins += 1
                print("Rock vs Paper - you lost :(" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
            elif ai == "scissors":
                player_wins += 1
                print("Rock vs Scissors - you won!" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
        elif player == "paper":
            if ai == "rock":
                player_wins += 1
                print("Paper vs Rock - you won!" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
            elif ai == "scissors":
                computer_wins += 1
                print("Paper vs Scissors - you lost :(" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
        elif player == "scissors":
            if ai == "rock":
                computer_wins += 1
                print("Scissors vs Rock - you lost :(" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
            elif ai == "paper":
                player_wins += 1
                print("Scissors vs Paper - you won!" +
                      "\nScores: {} - {}".format(player_wins, computer_wins))
    else:
        print("You need to make a choice!" +
              "\nScores: {} - {}".format(player_wins, computer_wins))

if player_wins == computer_wins:
    print("\nThe game ended in a draw.\nFinal Scores: {} - {}".format(player_wins, computer_wins))
elif player_wins > computer_wins:
    print("\nCongratulations, you won the game!\nFinal Scores: {} - {}".format(player_wins, computer_wins))
elif player_wins < computer_wins:
    print("\nSorry, you lost the game.\nFinal Scores: {} - {}".format(player_wins, computer_wins))
