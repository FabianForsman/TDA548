# package samples.usemoreclassesprint

from Person import Person


# The concept of a Car with an owner (a Person!)
# 
# self is a small OO model i.e. objects referencing
# other (concept) objects to build a model (abstraction) of the problem
# at hand
class Car:
    # Constructor
    def __init__(self, brand: str, id: str, year: int, mileage: float, owner: Person = None):
        self.brand = brand
        self.id = id
        self.year = year
        self.mileage = mileage
        self.owner = owner  # Connect self with other object

    def get_owner(self):
        return self.owner

    # Other setter and getters omitted, NOTE: Just add setters/getters if needed!
