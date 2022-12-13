#In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#Hangman Part 3

import random

#Part 1 Logic
def generateRandomWord():
    sowpods = list()
    
    with open('sowpods 30.txt', 'r') as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            sowpods.append(line)
    
    randomInt = random.randint(0, len(sowpods))
    return sowpods[randomInt]

if __name__=="__main__":
    print("Welcome to Hangman!")
    
    gameWord = generateRandomWord()
    gameWordManip = list()
    gameWordManip.extend(gameWord) #Extend iterates over its input, expanding the list, and adding each member.
    
    guessedCorrect = list()
    guessedLetters = set()
    guessNumber = 5
    
    print(gameWord)
    
    for x in range(len(gameWordManip)):
        guessedCorrect.append("_")
    
    while guessNumber != 0:
        print(*guessedCorrect)
        usrGuess = input("Guess your letter: ").capitalize()
        
        if usrGuess in guessedLetters:
            print("You already guessed that letter: Guess again!")
            continue
        else:
            correctGuess = 0
            for y in range(len(gameWordManip)):
                if gameWordManip[y] == usrGuess:
                    guessedCorrect[y] = usrGuess
                    correctGuess += 1
            
            if correctGuess == 0:
                guessNumber -= 1
                print("You have", guessNumber+1, "incorrect guesses left")
        
        if guessedCorrect == gameWordManip:
            print("The word was", ''.join(gameWordManip))
            break
    
    print("Game Over")