"""
CP1404 - Practical 06 - 3. Guitars
"""

from guitar import Guitar


def main():
    """Program to manage a list of guitars."""
    print("My guitars!")
    guitars = []

    # Get user input
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("\nName: ")

    # Testing
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    # Display
    if guitars:  # If list is not empty
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}"
                  f"{vintage_string}")
    else:
        print("\nNo guitars :( Quick, go and buy one!")


if __name__ == '__main__':
    main()
