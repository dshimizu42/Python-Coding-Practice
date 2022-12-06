import random

def generateRandomNumber():
    return random.randint(1000, 9999)

def splitNumber(split):
    result = []
    
    for x in str(split):
        result.append(int(x))
    
    return result

def checkCowsAndBulls(comp, guess):
    
    cows = bulls = 0
    unsolvedPos = []
    numbersSearched = set()
    
    for x in range(len(comp)):
        if (comp[x] == guess[x]):
            cows += 1
            numbersSearched.add(comp[x])
        else:
            unsolvedPos.append(x)
    
    for y in range(len(unsolvedPos)):
        for z in range(len(unsolvedPos)):
            if (comp[y] == guess[z]):
                for a in range(len(numbersSearched)):
                    temp = list(numbersSearched)
                    if temp[a] == comp[y]:
                        continue
                    else:
                        numbersSearched.add(comp[y])
                        bulls += 1
                    print("N: ", temp)
    
    print(cows, " cows, ", bulls, " bulls")
    return None

if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!")
    
    computerNumber = splitNumber(generateRandomNumber())
    usrGuess = None
    guessCount = 0
    
    while usrGuess != computerNumber:
        guessCount += 1     
        usrGuess = splitNumber(input("Enter a number: "))
        if len(usrGuess) != len(computerNumber):
            print("Try again: Enter a four digit number")
            continue
        else:
            print("C: ", computerNumber)
            checkCowsAndBulls(computerNumber, usrGuess)
 
    print("Congratulations! You guessed the correct number in ", guessCount, " guesses!")
