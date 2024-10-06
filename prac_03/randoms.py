"""
CP1404/CP5632 - Practical 3 - 2. Random Numbers
"""
# What did you see on line 1?
# 5, 19, 12 -> A random number between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# What did you see on line 2?
# 7, 3, 5 -> A random number between 3 and 10, stepping by 2.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4?
# No, it could not produce a 4 since it steps by 2 (results could be 3, 5, 7, or 9).

# What did you see on line 3?
# 4.4154489306127225, 2.803560349493035, 4.125957248467416 -> A random real number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Code that produces a random number between 1 and 100 inclusive.
import random
random_number = random.randint(1, 100)
print(random_number)