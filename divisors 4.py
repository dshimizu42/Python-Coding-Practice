#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

userNum = int(input('Enter any whole number: '))

space = range(1, userNum)
y = []

for num in space:
    remainder = userNum % num
    
    if remainder == 0:
        y.append(num)

print("Here are all the divisors of your number: " + str(y))