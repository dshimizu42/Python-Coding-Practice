#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

usrStr = input('Enter any string to test if it is a palindrome: ')

if usrStr[:] == usrStr[::-1]:
    print('This string is a palendrome')
else:
    print('This string is not a palendrome')