for num in range(1, 21):
    if num == 4 or num == 13:
        print("{} is unlucky".format(num))
    elif num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
