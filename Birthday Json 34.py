#modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
# Birthday Data Part 2

import json

if __name__=="__main__":
    
    with open("info.json", "r") as a:
        birthday = json.load(a)    
    
    while True:
        usrInput = input("Would you like to enter more names into the birthday list?: ").strip().lower()
        
        if usrInput == "yes":
            usrInputN, usrInputB = input("Please enter the name and birthday of a person, separated by a comma: ").split(',')
            birthday.update({usrInputN:usrInputB})
        elif usrInput == "no":
            break
        else:
            print("Invalid input. Please try again")
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    
    for keys, values in birthday.items():
        print(keys)
    
    while True:
        usrInput = input("Who's birthday do you want to look up?: ")
        
        if usrInput in birthday.keys():
            print("{}'s birthday is {}".format(usrInput, birthday[usrInput]))
            break
        else:
            print("Person not found. Please enter another name.")
    
    with open("info.json", "w") as f:
        json.dump(birthday, f)