"""
CP1404 - Practical 06 - Programming Languages
Estimate: 1h
Actual:
"""
class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize the ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "dynamic"