
name_file = open("name.txt", 'w')
name = str(input("please enter your name"))
print(name, file=name_file)
name_file.close()


name_file = open("name.txt", 'r')
print("Your name is", name_file.readline())
name_file.close()


number_file = open("numbers.txt", 'r')
for line in number_file:
    num_1 = number_file.readline()
    num_2 = number_file.readline()
    total = num_1 + num_2
    print(total)
number_file.close()


number_file = open("numbers.txt", 'r')
total = 0
for line in number_file:
    num = int(line)
    total += num
print(total)
number_file.close()
