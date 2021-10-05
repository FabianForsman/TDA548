# package samples.useaclass

from Complex import Complex


# This is for tests of the Complex class
def test_complex():
    # Create objects of type Complex
    c1 = Complex(1, 2)      # Instantiate, use constructor on right side
    c2 = Complex(-3, -5)
    c3 = Complex(c2)        # Use constructor to create a copy

    # c1.__re = 4      # Can't access, private instance variable!
    # c1.__img = 4     # Can't access, private!
 
    print(c1.get_real_part() == 1)    # Call methods to access
    print(c1.get_img_part() == 2)

    print(c3 == c2)
    print(c1 - c2 == Complex(4, 7))
    print(c1 + c1 + c1 == Complex(3, 6))

    # ---- Use Complex in collections ------------
    c_list = [Complex(1, 2), Complex(6, -1)]    # List of own objects
    print(c_list[0] - c_list[0] == Complex(0, 0))

    c_list.append(Complex(5, -2))
    print(Complex(5, -2) in c_list)      # Must have __eq__

    complex_msg = {Complex(0,0): "zero"}
    print(complex_msg[Complex(0,0)] == "zero")

    print(str(Complex(5, -2)) == "5.0 - 2.0i")


if __name__ == "__main__":
    test_complex()
