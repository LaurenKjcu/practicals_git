"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = int(input("sales: "))
while sales < 0:
    print("invalid")
    sales = int(input("sales: "))

if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("bonus is: ${}".format(bonus))

#############################################################

sales = int(input("sales: "))
while sales >= 0:

    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("bonus is: ${}".format(bonus))
    sales = int(input("sales: "))
