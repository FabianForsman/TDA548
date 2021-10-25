# package samples.inheritance

# Problem!  Classes have same instance variables and methods.
# Plenty of duplicated code!
# 
# To be continued: See Inheritance2
def inheritance_program():
    _dog = Dog("Lassie", 4)
    _cat = Cat("Misse", 5, False)


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):  # <-------- Duplicate
        return self.name

    def get_age(self):  # <-------- Duplicate
        return self.age


class Cat:
    def __init__(self, name: str, age: int, is_evil: bool):
        self.name = name
        self.age = age
        self.is_evil = is_evil

    def get_name(self):  # <-------- Duplicate
        return self.name

    def get_age(self):  # <-------- Duplicate
        return self.age

    def is_evil(self):
        return self.is_evil
