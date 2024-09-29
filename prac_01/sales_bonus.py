"""
CP1404 - Practical 1 - 1. Sales Bonus

Instructions:
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
THRESHOLD = 1000
get sales
while sales >= 0
    if sales < THRESHOLD
        bonus_rate = 0.1
    else
        bonus_rate = 0.15
    bonus_amount = sales * bonus_rate
    print bonus_amount
    get sales
"""
THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < THRESHOLD:
        bonus_rate = 0.1
    else:
        bonus_rate = 0.15
    bonus_amount = sales * bonus_rate
    print(f"Based on your sales {sales} your bonus is ${bonus_amount}")
    sales = float(input("Enter sales: $"))
