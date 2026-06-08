## Python MINI Project (Expenditure Calculator)!


## Inputs We Need from the  user.
# 1. Total Rent of flat/Room.
# 2. Total Amount of Food/Rasan.
# 3. Electricity Units Spend.
# 4. Charge Per Unit.
# 5. Other Expenses(Like Vegetables, Water, Some Other Things....)
# 6. Person Living In Flat/Room.

## What Will  be the Output 
# Total amount you've to pay is 

'''-----Now Take Step By Step Input that is Required-----'''

rent = int(input("Enter the Rent of flat/Room!"))

food_rasan = int(input("Enter the Amount of Food/Rasan!"))

electricity_spend = int(input("Enter the Total Number of Electricity Units"))

charge_per_unit = int(input("Enter the Charges per unit!"))

others_expenses = int(input("Enter the Other Expenses(Like Vegetables, Water, Some Other Things....)!"))

persons = int(input("Enter the Number of Persons Living In flat/Room!"))

total_bill = electricity_spend * charge_per_unit

output = (rent + food_rasan + total_bill + others_expenses) // persons

print(f"Each Person Will pay the total Amount is {output}.")