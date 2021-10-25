# package samples.types

# Casting to interface type is always allowed, even if NO super sub relation!
from abc import abstractmethod, ABC


def duck_type_cast_program():
    car = Car()
    s1: CanSpeak = car      # Warning that we'll get a runtime error ...
    # s1.say()              # AttributeError: 'Car' object has no attribute 'say'

    car = TalkingCar()
    s2: CanSpeak = car      # Warning, since we have no static guarantees that TalkingCar can speak.
    s2.say()                # But we know it can, and indeed there's no error when running.


class CanSpeak(ABC):
    @abstractmethod
    def say(self):
        raise NotImplementedError


class Car:
    # Class has **nothing** to do with CanSpeak!!!
    pass


# Subtype to Car, could have been subtype to CanSpeak
class TalkingCar(Car):
    def say(self):
        return "Honk honk"


if __name__ == "__main__":
    duck_type_cast_program()
