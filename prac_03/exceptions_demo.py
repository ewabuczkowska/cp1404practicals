"""
CP1404 - Practical 3 - 4. Exceptions Demo

Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. A ValueError will occur when the user inputs something that is not an integer,
# #    like letters or a decimal number.
# 2. A ZeroDivisionError will occur when the denominator is equal to 0.
# 3. Yes, by using an if else decision structure