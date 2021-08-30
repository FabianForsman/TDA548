# package exercises

from math import pi


# Program to calculate the surface area of a sphere
# See https://en.wikipedia.org/wiki/Sphere#Surface_area
#
# Formula is: area = 4 * pi * radius²     (kg/m²)
#
# See:
# - F2C
# - IO
# - PrimitiveVariables
# - Arithmetic
def calculate_sphere_area_program():
    # Write your code here
    print("Write your own code for calculating surface area")
    # --- Input ---------
    x = float(input("Enter the radius of your circle: "))
    # --- Process --------
    area = 4 * pi * x * x
    # --- Output ---------
    print("Surface area of circle is: ", area)


# Recommended way to make module executable
if __name__ == "__main__":
    calculate_sphere_area_program()
