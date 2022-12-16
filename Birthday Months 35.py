#load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
# Birthday Data Part 3

import json
from collections import Counter

def convertToMonth(num):
    allMonths = {'01': 'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
        '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'
        }
    
    return allMonths.get(num)
    

if __name__=="__main__":
    with open("info.json", "r") as jsonFile:
        birthday = json.load(jsonFile)
    
    print(birthday, end='\n\n')
    
    bdayMonths = []
    
    for months in birthday.values():
        bdayMonths.append(months.strip().split('/')[0])
    
    for x in range(len(bdayMonths)):
        bdayMonths[x] = convertToMonth(bdayMonths[x])
    
    c = Counter(bdayMonths)
    print(c)
    
    with open("info2.json", "w") as x:
        json.dump(c, x)