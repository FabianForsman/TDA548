# package exercises.ex2usemoreclasses

from Point import Point
from Triangle import Triangle


#  This is a test of Classes (objects of) Point and Triangle
#
#  See
#  - usemoreclasses
def test_point_triangle():
    # All should print true as usual
    
    # Point
    p = Point(1, 2, 3)
    print(p.distance(Point(p)) == 0)
    print(Point(0, 0, 0).distance(Point(1, 0, 0)) == 1)

    # Triangle uses Points!
    t = Triangle(Point(0, 0, 0), Point(0, 1, 0), Point(1, 0, 0))
    print(abs(t.area() - 0.5) < 0.000001)  # Area should be 0.5

    # Test data
    p1 = Point(1, 1, 1)
    p2 = Point(2, 2, 2)
    p3 = Point(3, 3, 3)
    triangles = [
        Triangle(p1, p2, p3),
        Triangle(p1, p3, p2),
        Triangle(p2, p1, p3),
        Triangle(p2, p3, p1)
    ]

    # Try to find triangle in list
    print(Triangle(p1, p2, p3) in triangles)
    print(Triangle(p3, p1, p2) not in triangles)


if __name__ == "__main__":
    test_point_triangle()
