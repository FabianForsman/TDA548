# package exercises.ex3theory

#  More subclasses and subclasses (objects) connected
#
#  See
#  - useaclass
#  - usemoreclasses
#  - usestatic
def theory_program():
    pass
    print("1. What will be printed? Why?")
    p1 = Pt()
    p2 = Pt()
    
    p1.x = 1
    p1.y = 2
    p2.x = 2 * p1.x # p2(x) = 2
    p2.y = 2 * p1.y # p2(y) = 4
    p3 = p1 # p3(x,y) = p1(x,y) = 1,2
    p1 = p2 # p1(x,y) = p2(x,y) = 2,4
    
    print(p1 == p2) #True
    print(p2 == p3) #False
    print(p1 == p3) #False
    
    print(p1.x == p2.x) #True
    print(p2.x == p3.x) #False
    print(p3.y == p1.y) #False

    print("2. What will be printed? Why? See Mth class below")
    m = Mth(3)
    m.op(1.5) # m.i = 4.5
    m.op() # m.i = 9.0
    m.op(2) # m.i = 11.0
    print(m.i)

    print("3. What will be printed? Why? How many objects are involved?")
    cc = Cainc(5) #cc.i = 5
    print(cc.do_it().do_it().do_it().do_it().i) # 5 objects. Print 9.

    print("4. What will be printed? Why? How many objects are involved?")
    c = CCtor(CCtor(CCtor(8)))
    print(c.i) # Prints 8. 3 objects

    print("5. Explain what happens on each row")
    A.a = A.b           # 1
    A.a = A().b         # 2
    A.b = A.a           # 3
    A().b = A.a         # 4
    A().a = A().b       # 5
    A().b = A().a       # 6
    a: A = None         # 7
    print(type(a).a)    # 8


# ---------- Classes ----------------------------
class A:
    a = 1    # Class variables
    b = 2


class Pt:
    def __init__(self):
        self.x = 0
        self.y = 0


class Mth:
    def __init__(self, i):
        self.i = i

    def op(self, i=None):
        if i is None:
            self.i *= 2
        else:
            self.i += i


class Cainc:
    def __init__(self, i):
        self.i = i

    def do_it(self):
        return Cainc(self.i + 1)


class CCtor:
    def __init__(self, o):
        if isinstance(o, CCtor):
            self.i = o.i
        elif isinstance(o, int):
            self.i = o


if __name__ == "__main__":
    theory_program()
