for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')

for num in range(20, 0, -1):
    print(num, end=' ')

n = int(input("n?"))
print("*" * n)
for i in range(1, n + 1):
    print("*" * i)
