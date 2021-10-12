# package exercises.ex1inheritance

from Classes import *


# Using classes, inheritance and overriding
# 
# Run this to get the printout requested i.e.
# 
# Car{topSpeed=160.0, {owner=Person{id='123', name='olle'}, id='abc'}}
# Van{maxCargo=400.0, {owner=Person{id='456', name='fia'}, id='def'}}
# Car{topSpeed=210.0, {owner=Person{id='456', name='fia'}, id='ghi'}}
# Van{maxCargo=800.0, {owner=Person{id='123', name='olle'}, id='jkl'}}
# 
# Car{topSpeed=160.0, {owner=Person{id='123', name='olle'}, id='abc'}}
# Van{maxCargo=400.0, {owner=Person{id='456', name='fia'}, id='def'}}
# Car{topSpeed=210.0, {owner=Person{id='456', name='fia'}, id='ghi'}}
# Van{maxCargo=800.0, {owner=Person{id='123', name='olle'}, id='jkl'}}
# See:
# - inheritance/
def test_car_van_program():
    p1 = Person("123", "olle")
    p2 = Person("456", "fia")

    vehicles = [Car(p1, "abc", 160),
                Van(p2, "def", 400),
                Car(p2, "ghi", 210),
                Van(p1, "jkl", 800)
                ]

    for v in vehicles:
        print(v)  # Each vehicle should know what to print!

if __name__ == "__main__":
    test_car_van_program()