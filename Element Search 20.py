#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def inList (orderedList, usrNum):
    
    # This for loop searches all the elements of the ordered list for the user's input number
    # It checks each element until the userNumber is found or not found
    # If it's found, return true. If not, then return false
    for x in range(len(orderedList)):
        if orderedList[x] == usrNum:
            return True
    return False


if __name__=="__main__":
    usrList = [1,2,3,4,5,6,7,8,9,10] #Initialized ordered list
    usrInput = int(input("Enter a number to see if it's in my list: ")) #Asking the user to input a number to check if it's in the initialized list
    print(inList(usrList, usrInput)) #Prints the list
