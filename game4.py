import random
n = random.randint(1, 10)


while True:
    Guess = int(input("What is the level?"))

    if Guess<n:
        print("Too Small")

    elif Guess>n:
        print("Too Large")

    else:
        print("Just Right!")
        break
