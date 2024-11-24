"""
CP1404  - Practical 09 - 2. Unreliable car
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Version of car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_reliability_number = random.randint(0, 100)
        if random_reliability_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0






