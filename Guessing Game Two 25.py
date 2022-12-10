#You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

import time

def newGuess(guess, nums): 
    compGuess = nums[int(len(nums)/2)] # Finding the middle element of the remaining elements in the list
    return compGuess

if __name__=="__main__":
    
    print("Welcome to the Guessing Game! Think of a number between 0 and 100...\n")
    time.sleep(2)
    print("The computer will now attempt to guess your number. When asked, enter higher, lower, or correct until your number is reached.\n")
    time.sleep(2)
    
    allNums = list(range(101))
    currGuess = 50
    possibleResp = ['higher', 'lower', 'correct'] # All possible user responses
    
    while True:
        usrInput = input("Is your number " + str(currGuess) + "?: ")
        if usrInput == possibleResp[0]:
            allNums = [elem for elem in allNums if elem > currGuess] # This code updates the current list with all elements greater than the current guess
            currGuess = newGuess(currGuess, allNums)
            continue
        elif usrInput == possibleResp[1]:
            allNums = [elem for elem in allNums if elem < currGuess] # This code updates the current list with all elements less than the current guess           
            currGuess = newGuess(currGuess, allNums)           
            continue
        elif usrInput == possibleResp[2]:
            break
        else:
            print("Try again. Please enter a valid response.")
    
    print("Your number was " + str(currGuess) + "! Thanks for playing.")

    # Call the computer guess function
    
    