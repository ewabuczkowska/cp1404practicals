"""
CP1404 - Practical 2 - Score Menu
"""


def main():
    score_value = 0  # Initialize score
    choice = ""

    while choice != "Q":
        display_menu()
        choice = input("Enter your choice: ").upper()  # Use .upper() for case insensitivity

        if choice == "G":
            score_value = get_valid_score()  # Get a valid score when the user chooses
        elif choice == "P":
            print_result(score_value)
        elif choice == "S":
            print_stars(score_value)
        elif choice == "Q":
            print("Thank you! Farewell!")
        else:
            print("Invalid choice!")


def display_menu():
    """ Display all menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def evaluate_score(score):
    """ Evaluate the previously entered score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    """ Get a valid score that is between the parameters of 0 to 100"""
    score = int(input("Enter your score (0-100): "))

    while score < 0 or score > 100:
        print("Enter a valid score!")
        score = int(input("Enter your score (0-100): "))

    return score


def print_result(score_value):
    """ Print results based on score value."""
    result = evaluate_score(score_value)
    print(f"The result for a score of {score_value} is: {result}")


def print_stars(score_value):
    """ Print stars based on score value."""
    stars = '*' * score_value
    print(stars)


main()
