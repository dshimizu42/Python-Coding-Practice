#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

usrInputs = set()
usrInput = None

while usrInput != "x":
    usrInput = input("Enter a name into the list. Enter \"x\" to exit: ")
    if usrInput == "x":
        break
    usrInputs.add(usrInput)
    
print(usrInputs)
