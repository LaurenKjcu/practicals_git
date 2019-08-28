total_price = 0
item_num = int(input("number of items:"))
while item_num < 0:
    print("invalid number of items")
    item_num = int(input("number of items:"))

for i in range(1, item_num + 1):
    price = float(input("price of item {}:".format(i)))
    total_price += price
if total_price > 100:
    total_price = total_price * .9
print("the total for {} items is ${:.2f}".format(item_num, total_price))
