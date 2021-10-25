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
        if type(args[0]) == Rational:
            self.num = args[0].num
            self.denom = args[0].denom
        else:
            num = args[0]
            if len(args) == 1:
                denom = 1
            else:
                denom = args[1]
            self.num, self.denom = self.check_fracture_reduction(num, denom)

    def get_num(self):
        return self.num

    def get_denom(self):
        return self.denom 

    def check_fracture_reduction(self, num: int, denom: int):
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
        if self.denom == other.denom:
            num = self.num + other.num
            denom = self.denom
        else:
            num = self.num * other.denom + other.num * self.denom
            denom = self.denom * other.denom
            num, denom = self.check_fracture_reduction(num, denom)
        return Rational(int(num), int(denom))
    
    def __sub__(self, other):
        if self.denom == other.denom:
            num = self.num - other.num
            denom = self.denom
        else:
            num = self.num * other.denom - other.num * self.denom
            denom = self.denom * other.denom
            num, denom = self.check_fracture_reduction(num, denom)
        return Rational(int(num), int(denom))

    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        num, denom = self.check_fracture_reduction(num, denom)
        return Rational(int(num), int(denom))

    def __div__(self, other):
        num = self.num / other.num
        denom = self.denom / other.denom
        num, denom = self.check_fracture_reduction(num, denom)
        return Rational(int(num), int(denom))

    def __truediv__(self, other):
        num = self.num / other.num
        denom = self.denom / other.denom
        num, denom = self.check_fracture_reduction(num, denom)
        return Rational(int(num), int(denom))

    def __lt__(self, other):
        return self.num / self.denom < other.num / other.denom

    def __float__(self):
        return float(self.num / self.denom)

    def __eq__(self, other) -> bool:
        return self.num == other.num and self.denom == other.denom

    def __call__(self):
        return (self.num, self.denom)

    def __hash__(self) -> int:
        return int(self.num / self.denom)

    def __str__(self) -> str:
        return f"{int(self.num)} / {int(self.denom)}"