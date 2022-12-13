#In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
#Hangman Part 1

import random

if __name__=="__main__":
    
    sowpods = list()
    
    with open('sowpods 30.txt', 'r') as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            sowpods.append(line)
    print("The entire file has been read!")
    
    randomInt = random.randint(0, len(sowpods))
    randomWord = sowpods[randomInt]
    
    print("The word chosen was", randomWord, "!", end="")