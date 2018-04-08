from random import randint
min_number = 1
max_number = 10
answer = randint(min_number, max_number)
player = None

print("\nWelcome to my Guessing Game!\n")
while player != "n":
    player = int(
        input("Guess a number between {} and {}: ".format(min_number, max_number)))
    if player < answer:
        print("Too low. Try again.")
    elif player > answer:
        print("Too high. Try again")
    else:
        print("\nCongratulations, you win!")
        while True:
            player = input("\nDo you want to play again? (y/n) ").lower()
            if player == "n":
                break
            elif player == "y":
                answer = randint(min_number, max_number)
                print("\nNew Game!\n")
                break
print("Thanks for playing. Bye!")
