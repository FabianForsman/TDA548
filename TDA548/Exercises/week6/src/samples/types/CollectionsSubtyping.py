# package samples.types


# Using super/sub types with collections
from typing import List
from abc import *


def super_sub_list_program():
    d = Dog("Fido", 3)
    c = Cat("Missan", 4, False)

    pets: List[Pet] = []
    pets.append(d)                  # Ok, Dog is a Pet
    pets.append(c)                  # Ok, Cat is a Pet
    pets[0].get_name()

    speakers: List[CanSpeak] = []
    speakers.append(d)              # Ok, Dog can speak
    speakers.append(c)              # Ok, Cat can speak
    speakers[0].say()
    speakers[0].get_name()          # No guarantee there is such a method!

    speakers = pets                 # Whoa, dangerous! (Why?)
    pets = speakers                 # This is even worse, but at least here we get a warning.

    pets.append(speakers[0])        # A speaker might not be a Pet!
    speakers.append(pets[0])        # But any pet can speak

    speakers.extend(pets)           # We can add all pets to a list of speakers
    pets.extend(speakers)           # ... but not all speakers to a list of pets

    for speaker in speakers:
        if isinstance(speaker, Pet):    # Check if object is Pet or subclass to
            pets.append(speaker)        # then we know we can add it safely


# --------------- Types -----------------
class CanSpeak(ABC):
    @abstractmethod
    def say(self):
        pass


class Pet(CanSpeak, ABC):
    def __init__(self,  name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Dog(Pet):
    def __init__(self, name, age):    # Redundant code gone
        super().__init__(name, age)

    def say(self):    # Dog is subtype to Pet and CanSpeak, must implement method!
        return f"{self.name} says Arf"


class Cat(Pet):
    def __init__(self, name, age, is_evil):
        super().__init__(name, age)
        self.is_evil = is_evil

    def is_evil(self):
        return self.is_evil()

    def say(self):
        return f"{self.name} says Meow"


if __name__ == "__main__":
    super_sub_list_program()
