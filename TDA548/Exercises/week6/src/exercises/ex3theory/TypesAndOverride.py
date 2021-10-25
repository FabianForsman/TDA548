# package exercises.ex3theory

from abc import ABC, abstractmethod


# Uncomment a)-h) one at the time and explain
# what happens and why.
# If no errors, what is printed out, explain why.
# 
# 
# Declared type affects only what PyCharm thinks is possible with a
# variable (i.e. which methods to call, checked compile time)
# 
# Object type decides which version of method (if overriding) should be called
# (decided runtime, dynamic dispatch)
#
# See:
# - inheritance
# - override
# - types
def test_override_program():
    # # a
    d = D()
    # c = d
    # c.do_it()

    # # b
    # iy: IY = D()
    # c1: C = iy
    # c1.do_other()

    # # c
    # a: A = B()
    # a.do_it()

    # # d
    # ix: IX = B()
    # iy3: IY = C()
    # ix = iy3
    # ix.do_it()

    # # e
    # a4: A = C()
    # d1: D = a4
    # d1.do_it()

    # # f
    # c2: C = D()
    # b: B = c2

    # # g
    # c3: C = C()
    # a1: A = c3
    # a1.do_other()

    # # h
    # iy2 = C()
    # iy2.do_other()


# # ---------- Interfaces and classes -------------------------
class IX(ABC):
    @abstractmethod
    def do_it(self):
        raise NotImplementedError


class IY(ABC):
    @abstractmethod
    def do_other(self):
        raise NotImplementedError


class A:
    def do_it(self):
        print(f"Doit A")


class B(A, IX):
    def do_it(self):
        print(f"Doit B")


class C(A, IY):
    def do_it(self):
        print(f"Doit C")

    def do_other(self):
        print(f"DoOther {type(self)}")


class D(C):
    def do_it(self):
        print(f"Doit D")


if __name__ == "__main__":
    test_override_program()
