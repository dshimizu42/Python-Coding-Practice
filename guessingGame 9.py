#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

target = random.randint(1, 9)

while True:
    usrGuess = int(input('Guess a number between 1 and 9: '))
    if usrGuess > target:
        print('Your guess was too high')
    elif usrGuess < target:
        print('Your guess was too low')
    else:
        print('You\'re correct! The number was ' + str(target))
        break;
print('Thanks for playing')

