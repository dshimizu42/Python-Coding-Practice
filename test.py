x = input('first number: ')
y = input('second number: ')
print (float(x) + float(y))

#This is being ignored cause Python loves pound signs

firstNum = int(input('first number: '))
op = input('PEMDAS: ')
secondNum = int(input('second number: '))

if op == '-':
    print(firstNum - secondNum)
elif op == '+':
    print(firstNum + secondNum)
elif op == '/':
    print(firstNum / secondNum)
elif op == '*':
    print(firstNum * secondNum)
else:
    print('ERROR: Enter +, -, *, /')