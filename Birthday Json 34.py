#modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
# Birthday Data Part 2

import json

if __name__=="__main__":
    
    birthdayDictionary = {
        "Albert Einstein": '03/14/1879',
        "Benjamin Frankin": '01/17/1706',
        "Ada Lovelace": '10/10/1815'
        }
    
    with open("info.json", "w") as f:
        json.dump(birthdayDictionary, f)
    
    with open("info.json", "r") as a:
        birthday = json.load(a)
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    
    for keys, values in birthday.items():
        print(keys)
    
    usrInput = input("Who's birthday do you want to look up?: ")
    
    if usrInput in birthday.keys():
        print("{}'s birthday is {}".format(usrInput, birthday[usrInput]))
    else: 
        print("Person not found. Please enter another name.")    