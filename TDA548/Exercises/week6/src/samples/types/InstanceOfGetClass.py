# package samples.types

from abc import *


# To examine types in running program operator isinstance or
# method getClass() may be used.
# 
# BUT! Avoid. Better use polymorphism (overriding).
# See: override/WhyOverride
def isinstance_program():
    c = Car()
    tc = TalkingCar()
    s: CanSpeak = tc

    print(isinstance(c, Car))  # Is c Car or subtype of?
    print(isinstance(tc, Car))
    print(isinstance(s, Car))

    print(not isinstance(c, TalkingCar))
    print(isinstance(tc, TalkingCar))
    print(isinstance(s, TalkingCar))

    print(type(c) == Car)  # What's the type of the object?
    print(type(tc) == TalkingCar)
    print(type(s) == TalkingCar)

    c = tc
    print(type(c) == TalkingCar)

    print(type(tc) != Car)


class CanSpeak(ABC):
    @abstractmethod
    def say(self):
        raise NotImplementedError


class Car:
    pass


class TalkingCar(Car, CanSpeak):
    def say(self):
        return "Honk honk"


if __name__ == "__main__":
    isinstance_program()
