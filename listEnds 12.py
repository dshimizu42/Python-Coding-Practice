#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

a = []

while True:
    c = input("Enter a number to add to the array. Type x to exit: ")
    if c == "x":
        break
    a.append(c)

#a = [5, 10, 15, 20, 25]
b = [a[0], a[len(a)-1]]
print(b)