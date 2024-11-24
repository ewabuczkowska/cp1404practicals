"""
CP1404  - Practical 09 - 2. Unreliable car
"""
from prac_09.unreliable_car import UnreliableCar


test_car = UnreliableCar("Unreliable car 1", 100, 50)
distance = test_car.drive(40)
print(distance)