print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# (bill / people) * (1.0 + (tip / 100)) = total and then I need to round it to the nearest 100th
total = (bill / people) * (1.0 + (tip / 100))
split = round(total, 2)
print(f"Each person should pay {split}")
