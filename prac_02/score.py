"""
CP1404 - Practical 2 - ScoreS
"""
import random

def main():
    user_score = float(input("Enter score: "))
    result = evaluate_score(user_score)
    print(f"Result: {result}")

    random_score = random.randint(0, 100)  # Generates a random integer between 0 and 100
    print(f"Random Score: {random_score:.2f}")
    print(f"Result: {evaluate_score(random_score)}")

def evaluate_score(score):
    """ Evaluate the previously gotten score. """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()