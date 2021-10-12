# package samples.override

# This is a motivation for using overriding.

def override_program():
    pets = [Cat(), Dog(), Dog(), Cat()]

    # Non overriding style, if new type of Pet added we would have to change this code,
    # add an else if clause. This could possible spread to many parts of program!
    for pet in pets:
        if isinstance(pet, Cat):  # Is p a Cat or any subtype of?
            print("Mjau")
        elif isinstance(pet, Dog):
            print("Voff")
        else:
            print("Unknown pet")

    # Using overriding, each Pet know what to say, if pets no change to code!
    # The objects know how to behave!
    for pet in pets:
        print(pet.say())


# ------------- Classes ---------------------
class Pet:
    def say(self):
        return "Unknown pet"


class Dog(Pet):
    def say(self):
        return "Voff"


class Cat(Pet):
    def say(self):
        return "Mjau"


if __name__ == "__main__":
    override_program()
