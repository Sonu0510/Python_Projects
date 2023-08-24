import random

def guessNum(a):
    random_number = random.randint(1, a)
    guessNum = 0

    while guessNum != random_number:
        guessNum = int(input(f"Enter a number between 1 and {a}: " ))

        if guessNum < random_number:
            print("Guessed Num is low than expected")

        elif guessNum > random_number:
            print("Guessed Num is more than expected")

    print("Got the right number, cogratulations!")

guessNum(10)


