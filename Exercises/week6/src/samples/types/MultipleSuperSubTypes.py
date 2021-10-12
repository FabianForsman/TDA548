# package samples.types

# Any class may have multiple super or subtypes
# Nothing to run here
class IX:
    pass


class IY:
    pass


class A:
    pass


# Multiple supertypes (A, IX, IY)
class B(A, IX, IY):
    pass


# Multiple subtypes to IX
class C1(IX):
    pass


class C2(IX):
    pass


class C3(IX):
    pass


# Multiple subtypes to A
class D1(A):
    pass


class D2(A):
    pass
