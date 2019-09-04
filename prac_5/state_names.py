STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state.upper() in STATE_NAMES:
        print("{:<4} is {:<}".format(state, STATE_NAMES[state.upper()]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

for state in STATE_NAMES:
    print("{:<4} is {:<}".format(state, STATE_NAMES[state]))
    """"""
