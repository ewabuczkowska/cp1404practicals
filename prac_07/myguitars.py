"""
CP1404 - Practical 07 - 3. More Guitars
"""
from prac_07.guitar import Guitar


def main():
    """Read guitars from file, get user input for new guitars, and save all guitars."""
    guitars = load_guitars()
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("\nName: ")

    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Load guitars from file and return list of Guitar objects."""
    guitars = []
    with open("guitars.csv") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def save_guitars(guitars):
    """Save all guitars to file."""
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display all guitars."""
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