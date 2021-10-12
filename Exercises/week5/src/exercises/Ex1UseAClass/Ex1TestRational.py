# package exercises.ex1useaclass

from Rational import Rational  # from the file Rational import the class Rational


# Test for Rational class (objects of type Rational)
# Make test print true for all print()
def test_rational():
    # As usual, all output should print true
    r = Rational(2)
    print(r.get_num() == 2 and r.get_denom() == 1)
    r = Rational(4, 9)
    print(r.get_num() == 4 and r.get_denom() == 9)
    r = Rational(49, 168)
    print(r.get_num() == 7 and r.get_denom() == 24)     # Always shortest form
    r = Rational(20, 4)
    print(r.get_num() == 5 and r.get_denom() == 1)
    r = Rational(0, 1)
    print(r.get_num() == 0 and r.get_denom() == 1)
    r = Rational(-49, 168)
    print(r.get_num() == -7 and r.get_denom() == 24)
    r = Rational(49, -168)
    print(r.get_num() == -7 and r.get_denom() == 24)
    r = Rational(-49, -168)
    print(r.get_num() == 7 and r.get_denom() == 24)

    r1 = Rational(1, 4)
    r2 = Rational(1, 2)
    print(r1 + r2 == Rational(3, 4))  # Requires overriding __add__ (and __eq__)
    print(r1 - r2 == Rational(-1, 4)) # Requires overriding __sub__
    print(r1 * r2 == Rational(1, 8))  # Requires overriding __mul__
    print(r1 / r2 == Rational(1, 2))  # Requires overriding __div__
    r3 = Rational(r1)
    print(r3 == r1)                         # Requires overriding __eq__
    print(not r3 < r1)                      # Requires overriding __lt__
    print(abs(float(r3) - 0.25) < 0.000001) # Requires overriding __float__

    r_list = [Rational(2, 3)]
    print(Rational(2, 3) in r_list)  # Requires overriding __eq__

    rational_msg = {}
    rational_msg[Rational(1,1)] = "one"         # Requires overriding __hash__
    print(rational_msg[Rational(1,1)] == "one")

    print(f"{Rational(6, 1)}" == "6 / 1")       # Requires overriding __str__


if __name__ == "__main__":
    test_rational()
