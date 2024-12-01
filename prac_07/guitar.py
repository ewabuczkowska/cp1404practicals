"""
CP1404 - Practical 07 - 3. More Guitars
"""


class Guitar:
    CURRENT_YEAR = 2024

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare the year for sorting Guitars."""
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar."""
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

