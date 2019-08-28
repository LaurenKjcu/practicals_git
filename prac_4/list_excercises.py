usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("username:")
if name in usernames:
    print("access granted")
else:
    print("access denied")

numbers = []
for i in range(0, 5):
    num = int(input("enter a number:"))
    numbers.append(num)
print("the largest number is".format(max(numbers)))
print("the smallest number is".format(min(numbers)))
print("the average is {}".format(sum(numbers) / 5))
print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[-1]))
