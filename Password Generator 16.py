#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random
import string

#Idea is to have 4 generator clauses: lowercase letters, uppercase letters, numbers 0-9, and symbols
#have a random number generator choose one of the clauses to generate a random ascii character
#repeat for a set number of characters

def passGenerator(usrInt):
    
    usrPass = []
    
    for a in range(usrInt):
        usrPass.append(randomCharacter())
    
    print("".join(str(elem) for elem in usrPass))
    return None

def randomCharacter():
    
    choose = random.randint(0, 3)
    
    if choose == 0:
        return random.randint(0, 9)
    elif choose == 1:
        return random.choice(string.ascii_uppercase)
    elif choose == 2:
        return random.choice(string.ascii_lowercase)
    elif choose == 3:
        return random.choice(string.punctuation)

if __name__=="__main__":
    
    passGenerator(int(input("Welcome to the Password Generator! Please enter the number of characters you'd like your password to be: ")))
