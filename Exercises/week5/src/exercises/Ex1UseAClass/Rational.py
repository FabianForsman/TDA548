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
        print(args)
        print(args[0])
        print(len(args))
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
        print(num, denom)
        if denom == None:
            denom = 1
        for i in range(2, round(sqrt(num))):
            if num % i == denom % i:
                num = num/i
                denom = denom/i
        return num, denom