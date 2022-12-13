#load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
# Birthday Data Part 3

import json

if __name__=="__main__":
    with open("birthdayPart3.json", "r") as a:
        birthday = json.load(a)
    
    birthdayDictionary = birthday
    
    
