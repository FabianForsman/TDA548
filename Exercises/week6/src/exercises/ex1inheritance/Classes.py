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
    pass
    # TODO


class Car:
    pass
    # TODO


class Van:
    pass
    # TODO

