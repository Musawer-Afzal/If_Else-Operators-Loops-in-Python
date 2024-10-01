import random


jackpot = random.randint(1,100)
print(jackpot)
guess = int(input("Guess a Number: "))
counter = 1
while guess != jackpot:
    if guess == jackpot:
        print("You guessed it right, Hurray!!!")
    elif guess < jackpot:
        print("Guess a higher number")
        guess = int(input("Guess a Number: "))
        counter += 1
    else:
        print("Guess a lower number")
        guess = int(input("Guess a Number: "))
        counter += 1