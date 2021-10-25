# package exercises.ex1inheritance

# Class for Persons (owners of Vehicles)
#
# **** Nothing to do here ***
from abc import ABC


class Person:
    def __init__(self, id_code, name):
        self.__id_code = id_code
        self.__name = name

    def __str__(self):
        return "Person{id='" + self.__id_code + "', name='" + self.__name + "'}"


class Vehicle(ABC):
    def __init__(self, person: Person, id: str, max: int, word: str):
        self.id = id
        self.word = word 
        self.max = float(max)
        self.person = person

    def __str__(self):
        return (type(self).__name__ + "{" + self.word + "=" + str(self.max) 
                + ", {owner=" + self.person.__str__() + ", id='" + self.id + "'}}")

class Car(Vehicle):
    def __init__(self, person: Person, id: str, max: int):
        super().__init__(person, id, max, "topSpeed")


class Van(Vehicle):
    def __init__(self, person: Person, id: str, max: int):
        super().__init__(person, id, max, "maxCargo")
