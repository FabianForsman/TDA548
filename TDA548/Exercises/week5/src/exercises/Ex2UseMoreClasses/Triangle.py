# package exercises.ex2usemoreclasses

from Point import Point
from math import *
# A class for a Triangle in 3D - should use Point class and Heron's formula
# NOTE: No IO here, this is just the logical concept.
# To test, run Ex2TestPointTriangle
class Triangle(Point):
    # TODO
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a: float = self.p1.distance(self.p2)
        b: float = self.p1.distance(self.p3)
        c: float = self.p2.distance(self.p3)
        s: float = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def __eq__(self, other) -> bool:
        return self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3