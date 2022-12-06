#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.

usrNum = int(input('Enter a number: '))

usrNum = usrNum % 4;

if usrNum == 0:
    print ('The number you entered is a multiple of 4')
elif usrNum == 1 or usrNum == 3:
    print ('The number you entered is odd\n')
else:
    print ('The number you entered is even\n')

num = int(input('Enter a number to check: '))
check =  int(input('Now, enter a number to divide the previous number by: '))

result = num % check

if result == 0:
    print('The numbers you entered divide evenly')
else:
    print('The numbers you entered don\'t divide evenly')
        
