# package exercises.ex2usemoreclasses
# A class for points in 3D. Should be considered immutable, no mutating methods
# NOTE: No IO here, this is just the logical concept.
# To test, run Ex2TestPointTriangle
from math import *
class Point():
    # TODO
    def __init__(self,*args):
        if isinstance(args[0], Point):
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def distance(self, other):
        dx = float((self.x - other.x))**2
        dy = float((self.y - other.y))**2
        dz = float((self.z - other.z))**2
        d = sqrt(dx + dy + dz)
        print(d)
        return d