"""Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75           """

cents = int(input("enter cents pr kWh:"))
daily_use = float(input("enter daily use in kWh:"))
billing_days = int(input("enter number of billing days:"))
bill = cents * daily_use * billing_days
print("estimated bill: ${:.2f}".format(bill))
