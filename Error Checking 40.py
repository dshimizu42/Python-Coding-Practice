#if the user does not enter a number between 1 and 9, tell them. Don’t count this guess against the user when counting the number of guesses they used.

import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess < 1 or guess > 9:
            print("Guess again!")
        else:
            number_of_guesses += 1
        if guess == number:
            break
    except ValueError:
        print("Please enter a valid number!")
print(f"You needed {number_of_guesses} guesses to guess the number {number}")
