# package samples.usemoreclasses;

from Car import Car
from Person import Person


# Using a small OO model with two classes, Car and Person
def test_car_person():

    # Create the model
    p = Person("Sven", 50,  500_000)
    # NOTE: Car doesn't create the owner, owner is passed in via constructor!
    c = Car("Volvo", "XMM176", 2016, 1.754, p)  # Set owner!!!

    # Use the model
    print(p.get_name() == "Sven")
    print(not c.get_owner().is_retired(65))


if __name__ == "__main__":
    test_car_person()
