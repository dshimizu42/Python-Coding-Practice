#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

userNum = int(input('Enter any whole number: '))

space = range(1, userNum) # Defining the range of integers in space variable
y = []

for num in space:
    remainder = userNum % num # Taking the modulous to deterimine the remainder of the numbers in the range
    
    if remainder == 0:
        y.append(num)

print("Here are all the divisors of your number: " + str(y))