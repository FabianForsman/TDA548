# package exercises.ex1useaclass

#    A class representing a rational number
#
#    NOTE: No IO here, this is just the logical concept.
#
#    Test the class by running Ex1TestRational.
#
# See:
# - useaclass/
# - UseADict
from math import sqrt
class Rational:
    # TODO implement class

    def __init__(self, *args):
        num = args[0]
        if len(args) == 1:
            denom = 1
        else:
            denom = args[1]
        
        (self.num, self.denom) = self.check_fracture_reduction(num, denom)

    def get_num(self):
        return self.num

    def get_denom(self):
        return self.denom 

    def check_fracture_reduction(self, num: int, denom: int):
        if denom == None:
            denom = 1
        greatest = self.gcd(num, denom)
        num /= greatest
        denom /= greatest
        return num, denom

    def gcd(self, num: int, denom: int) -> int:
        while not denom == 0:
            temp = denom
            denom = num%denom
            num = temp
        return num

    def __add__(self, other):
        return (self.num / self.denom) + (other.get_num() / self.get_denom())

    def __sub__(self, other):
        return (self.num / self.denom)-+ (other.get_num() / self.get_denom())
    def __eq__(self, o: object) -> bool:
        pass