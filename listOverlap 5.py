#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []

for elem in a:
    if elem in b:
        if elem not in result:
            result.append(elem)
print(str(result))

#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

c = random.sample(range(1, 100), random.randint(1,20))
d = random.sample(range(1, 100), random.randint(1,20))
resultList = []

print("Here is the first list of random numbers: " + str(c))
print("Here is the second list of random numbers: " + str(d))

for element in c:
    if element in d:
        if element not in resultList:
            resultList.append(element)
print(str(resultList))