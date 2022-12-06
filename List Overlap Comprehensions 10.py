#Write a program that returns a list that contains only the elements that are common between the lists (without duplicates)
import random

a = random.sample(range(100), 20)
b = random.sample(range(100), 15)

x = [z for y in a for z in b if z==y]

print(str(a))
print(str(b))
print(str(x))
