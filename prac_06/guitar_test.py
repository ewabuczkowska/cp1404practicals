"""
CP1404 - Practical 06 - 3. Guitar
"""
from guitar import Guitar

# Create two guitars
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 1512.9)

# Test get_age() method
print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
print(f"{another.name} get_age() - Expected 11. Got {another.get_age()}")

# Test is_vintage() method
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")