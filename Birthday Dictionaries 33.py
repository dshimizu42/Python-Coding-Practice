#keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays.
# Birthday Data Exercise Part 1

if __name__=="__main__":
    
    birthdayDictionary = {
        "Albert Einstein": '03/14/1879',
        "Benjamin Frankin": '01/17/1706',
        "Ada Lovelace": '10/10/1815'
        }
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    
    for keys, values in birthdayDictionary.items():
        print(keys)
    
    usrInput = input("Who's birthday do you want to look up?: ")
    
    if usrInput in birthdayDictionary.keys():
        print("{}'s birthday is {}".format(usrInput, birthdayDictionary[usrInput]))
    else: 
        print("Person not found. Please enter another name.")