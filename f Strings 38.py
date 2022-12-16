#Create a program that asks the user to enter their name and their age using f strings

userName = input('Hello!  What is your name?: ')
userAge = int(input('How old are you?: '))

if userAge < 100:
    userAge = 2021 + (100 - userAge)
    print(f"{userName} will turn 100 years old in {userAge}")
else:
    print(f"{userName} is over 100 years old")