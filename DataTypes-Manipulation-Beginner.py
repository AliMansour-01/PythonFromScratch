#Data Types and String Manipulation

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_to_split = int(input("How many people to split the bill?"))

tip = tip_amount / 100
split_bill = bill / people_to_split

final_bill = round((split_bill + (split_bill * tip)),2)

print(f"Each person should pay: {final_bill}")