"""
CP1404  - Practical 09 - 1. Test Taxi
"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"{my_taxi}, current fare: ${my_taxi.get_fare()}")