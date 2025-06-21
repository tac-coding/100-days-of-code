# Introduce tip calculator
print("Calculate your desired tip!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people are splitting the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_pp = total_bill / people
total = round(bill_pp, 2)

print(f"The total each person should pay is: ${total}")
