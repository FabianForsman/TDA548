# package samples.override

from multipledispatch import dispatch


# (Type-based) overloading and overriding in Python do not play all that well together.
#
def overload_program():
    the_a = A()
    the_b = B()

    the_a.do_it(1.0)    # Match do_it() in A if 1 -> 1.0 (super to sub allowed)
    the_b.do_it(1)      # Optimal method in object type (B) not selected
    the_b.do_it(1.0)    # Method inherited


# ------------- Types ---------------------
class A:
    @dispatch(float)
    def do_it(self, f):
        print("A do_it float")


class B(A):
    # NOT overriding, Inheritance and overloading
    @dispatch(int)
    def do_it(self, i):
        print("B do_it int")

    # If we were to comment out this method, we would still not
    # inherit the method from A. The @dispatch decorators are
    # resolved *after* overriding, which causes problems.
    @dispatch(float)
    def do_it(self, f):
        print("B do_it float")
        return f


if __name__ == "__main__":
    overload_program()
