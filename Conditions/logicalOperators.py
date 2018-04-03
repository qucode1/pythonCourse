# age = int(input("Age: \n"))
# if age <= 2:
#     print("Free entree for infants")
# elif age > 2 and age < 8:
#     print("child discount")
# else:
#     print("normal price")

# city = input("Where do you live:\n")
# if city == "los angeles" or city == "san fransisco":
#     print("You live in california!")
# else:
#     print("You live somewhere else")

age = int(input("What is your age?\n"))
if not(age <= 8 or age >= 65):
    print("You pay the normal price")
elif age >= 2 and age <=8:
    print("You get the child discount")
elif age >= 65:
    print("You get the senior discount")
else:
    print("You are an infant and get in for free")
