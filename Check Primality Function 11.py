#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.)

def determine_prime():
    return int(input("Enter a number to check if it is a prime number: "))

def calculate_Prime(a):
    listRange = list(range(1,a+1))
    
    divisorList = []

    for number in listRange:
        if a % number == 0:
            divisorList.append(number)
    
    return len(divisorList)
    
#Code Starts Here

usrInput = determine_prime()

arrayLength = calculate_Prime(usrInput)
    
if arrayLength > 2:
    print("The number you entered is not prime.")
else:
    print("The number you entered is prime.")
