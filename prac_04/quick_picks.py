"""
CP1404 - Practical 4 - 6. "Quick Pick" Lottery Ticket Generator
"""
import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(number_of_picks)
    print_quick_picks(quick_picks)


def generate_quick_picks(number_of_picks):
    """Generate random quick picks."""
    quick_picks = []
    for i in range(number_of_picks):
        numbers = set()
        while len(numbers) < NUMBERS_PER_PICK:
            numbers.add(random.randint(MIN_NUMBER, MAX_NUMBER))
        quick_picks.append(sorted(numbers))
    return quick_picks


def print_quick_picks(quick_picks):
    """Print and format quick picks."""
    for pick in quick_picks:
        formatted_pick = ' '.join(f'{num:2}' for num in pick)
        print(formatted_pick)


main()
