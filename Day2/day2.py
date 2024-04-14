# Tip Calculator

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
rounded_bill = round(float(bill), 2)
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_amount = rounded_bill * (tip_percentage / 100)
people = int(input("How many people to split the bill? "))
bill_per_person = rounded_bill + tip_amount
split = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${split}")