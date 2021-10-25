# package exercises.ex3theory
from abc import ABC


# See:
# - inheritance
# - types
# - override
#
# Uncomment each row in turn and explain why the row gives a warning or not.
def test_subtypes_program():
    ia: IA = A()
    ia = B()
    ia = C()
    ia = D()
    ia = E()

    a: A = A()
    a = B()
    a = C()
    a = D()
    a = E()

    b: B = B()
    b = A()
    b = C()
    c: C = C()
    c = D()
    c = E()
    d: D = D()
    d = E()
    e: E = E()
    e = C()
    e = D()


# -------------  Interfaces and classes ----------------------

class IA(ABC):
    pass


class A(IA):
    pass


class B(IA):
    pass


class C(A):
    pass


class D:
    pass


class E(D, IA):
    pass


if __name__ == "__main__":
    test_subtypes_program()
