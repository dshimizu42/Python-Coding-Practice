# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

def usrInputManip(usrInput):
    coordManip = usrInput.split(",")
    
    for x in range(len(coordManip)):
        usrInput[x].strip()
    
    coordManip = list(map(int, coordManip))
    return coordManip

if __name__=="__main__":
    
    print("This program will determine the greatest of three numbers")
    
    usrInput = usrInputManip(input("Please enter three numbers, separated by commas: "))
    highestNum = int()
    
    for x in range(len(usrInput)):
        if usrInput[x] >= highestNum:
            highestNum = usrInput[x]
    
    print("The highest number entered was",highestNum,"!")