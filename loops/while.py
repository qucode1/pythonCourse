# user_response = None
# while user_response != "please":
#     user_response = input("Ah, you didn't sa the magic word: ").lower()

# num = 1
# while num < 11:
#     print(num)
#     num += 1

# num = 1
# while num < 11:
#     output = ""
#     for x in range(0, num):
#         output += "\U0001f600 "
#     print(output)
#     num += 1

# while num < 11:
#     print("\U0001f600 " * num)
#     num += 1

phrase = "Hey, how's it going? "
while phrase.lower().find("stop copying me") == -1:
    phrase = input("Anonymous: " + phrase + "\nYou: ")
print("Ugh, fine you win.")
