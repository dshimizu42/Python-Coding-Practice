#Create a program that asks the user to enter their name and their age using f strings
#Print out a message addressed to them that tells them the year that they will turn 100 years old), except don’t explicitly write out the year. Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.

import datetime
import time

if __name__=="__main__":
    userName = input('Hello!  What is your name?: ')
    userAge = int(input('How old are you?: '))

    if userAge < 100:
        usrAge = datetime.datetime.now().year + (100 - userAge)
        print(f"{userName} will turn 100 years old in {usrAge}")
    else:
        print(f"{userName} is over 100 years old")
