"""
CP1404 - Practical 1 - Shop Calculator

Pseudocode:
DISCOUNT = 0.1
get number_of_items
total_price = 0
for i in number_of_items
    get item_price
    total_price = total_price + item_price
if total_price < 100
    total_price = total_price - (total_price * DISCOUNT)
print total_price
"""
DISCOUNT_RATE = 0.1 # Discount = 10%
total_price = 0
number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
