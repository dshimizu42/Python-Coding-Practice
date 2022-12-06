#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

userName = input('Hello!  What is your name?: ')
userAge = int(input('How old are you?: '))

if userAge < 100:
    userAge = 2021 + (100 - userAge)
    for x in range(0, 4):
        print(userName + " will turn 100 years old in " + str(userAge))
else:
    print(userName + " is over 100 years old")