# package samples.types


# When do we get a TypeError?
#
# Python allows us to cast values and treat them as any type, as long as
# the method calls exist (known as "Duck Typing"). But that means we always
# have the responsibility to ensure that types match.
#
# Types are checked during execution; in general we can't know the type of an object,
# it could have been created randomly.
import random


def type_cast_program():
    a = A()
    c: C = a        # Warning that we should have listened to...
    # c.do_it()     # AttributeError! Type of object a isn't a subtype of C, so do_it doesn't exist

    a = D()
    c: C = a        # No warning, now the object type (D) is a subtype!
    c.do_it()       # This call will always work

    a = get_it()    # Compiler can't know object type in the general case
    c: C = a        # ... but we don't even get a warning here.
    c.do_it()       # Maybe we get an AttributeError, maybe we don't...


class A:
    pass


class B(A):
    pass


class C(B):
    def do_it(self):
        print("Do IT!")


class D(C):
    pass


# NOTE: A method may return any subtype of return type
def get_it():
    r = random.randint(1, 4)
    switcher = {
        0: A(),
        1: B(),
        2: C(),
    }
    x = switcher.get(r, D()) # We don't know type of object!
    return x


if __name__ == "__main__":
    type_cast_program()
