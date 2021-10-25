# package samples.usemoreclasses


# The concept of a person
class Person:

    # We can overload through default arguments
    def __init__(self, name='', age=0, income=0):
        self.__name = name
        self.__age = age
        self.__income = income
    
    # ---- Getters and setters ------
    def get_name(self) -> str:
        return self.__name
    # No setter, name is final

    def set_age(self, age):
        self.__age = age

    def get_age(self) -> int:
        return self.__age

    def set_income(self, income):
        self.__income = income

    def get_income(self) -> int:
        return self.__income

    # Objects have the data to be able to answer questions!
    def is_retired(self, retiring_age: int):
        return self.__age >= retiring_age

    # __str__, __eq__ and __hash__ omitted
