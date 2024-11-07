"""
CP1404 - Practical 07 - 3. Guitars
"""
from prac_07.guitar import Guitar


def main():
    """Read file of guitars and display them."""
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)


def load_guitars():
    """Load guitars from file and return list of Guitar objects."""
    guitars = []
    with open("guitars.csv") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    print("My guitars:")
    for guitar in guitars:
        if guitar.is_vintage():
            print(f"{guitar} (vintage)")
        else:
            print(guitar)


if __name__ == '__main__':
    main()
