#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def reverseString(usrInput): #Defining a function to reverse the string
    tmp = usrInput.split() #Temporary list to split the string into english words without the whitespace
    stringLength = len(tmp) #temporary variable to cacluate the number of english words entered by the user
    newString = [] #String to output the reverse of what the user input
    
    for x in tmp: #for loop that defines temporary variable "x" and tmp, the length of the string entered by the user
        newString.append(tmp[stringLength-1]) #appending the list variable containing the reverse string, by iterating from the last english word entered by the user
        stringLength -= 1 #decreases the temporary variable by one to move to the second to last word entered by the user
    
    print(" ".join(newString)) #Joining strings together by a space and printing it backward

reverseString(input("Enter a sentence to have it repeated backward: ")) #Request the user to input a string to reverse its elements