finished = False
integer = 0
while not finished:
    try:
        integer = int(input("please enter an integer"))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", integer)
