#Code the fibonacci sequence. Remember to ask the user how many numbers in the sequence to generate

def calculateFibonacci(usrNumber):
    fArray = []
    
    current = 0
    new = 0
    previous = 1
    
    while usrNumber != 0:
        new = current + previous
        
        fArray.append(new)
        previous = current
        current = new
        
        usrNumber = usrNumber - 1
    
    return fArray

usrInput = int(input("Enter the number of Fibonnaci numbers to generate: "))
print(calculateFibonacci(usrInput))