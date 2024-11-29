"""
CP1404 - Practical 09 - Band class
"""


class Band:
    """Band class that contains musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musicians collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians playing their first instruments."""
        return '\n'.join(musician.play() for musician in self.musicians)
