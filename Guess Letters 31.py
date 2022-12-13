#write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
#Hangman Part 2
import random

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
    
    guessedLetters = list()
    
    for x in range(len(gameWordManip)):
        guessedLetters.append("_")
    
    while guessedLetters != gameWordManip:
        print(*guessedLetters)
        usrGuess = input("Guess your letter: ").capitalize()
        
        for y in range(len(gameWordManip)):
            if gameWordManip[y] == usrGuess:
                guessedLetters[y] = usrGuess
    
    print("The word was", ''.join(guessedLetters))
    