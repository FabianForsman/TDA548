"""
Denna exempeltenta är uppdelad i två delar, A och B.

För att nå godkänt betyg (3) på tentan krävs 24 poäng, av 32 möjliga, på del A.
Poängen på del B spelar ingen roll om du inte når dessa 24 poäng på del A.

För högre betyg än 3 avgörs betyget av summan på del A och del B; för betyg 4
krävs sammanlagt minst 36 poäng, och för betyg 5 krävs sammanlagt minst 48
poäng av 60 möjliga totalt.
"""


# ------- DEL A ------- #

""" Uppgift A1: 3p
Förklara med egna ord: Vad är skillnaden mellan en for- och while-loop?
Ge också exempel eller generell tumregel för när de olika kan användas.
"""


def uppgiftA2():
    """
    Uppgift A2: 4p
    Förklara noggrant steg för steg hur variabeln x får det värde som skrivs
    ut, och vilket värde.
    """
    x = 0
    for a in range(3):
        for b in range(3):
            x += 1
            if b == 1:
                break
    print(x)


def uppgiftA3():
    """ Uppgift A3: 6p
    Rita en bild som visar variabler, värden, referenser och objekt samt hur dessa
    förhåller sig till varann före anropet av metoden do_it(), och vad som ändras
    av anropet.
    """
    a = A(1)  # Before
    do_it(a)  # The call
    print(a)  # After

def do_it(a):
    a.b.x[a.i] = 7

class A:
    def __init__(self, i):
        self.i = i
        self.b = B(2)

class B:
    def __init__(self, length):
        self.x = [0] * length


""" Uppgift A4: 6p
Presentera en algoritm för en funktion as_set(in_list) som returnerar en ny
lista, där alla element i in_list finns i resultatlistan, men utan att något
element duplicerats (dvs gör om listan till en "mängd"). 

Presentera ditt svar som ett flödesschema, eller som pseudo-kod ("kodskiss"),
eller som faktisk kod i valfritt (känt) programmeringsspråk.
"""


""" Uppgift A5: 4p
Förklara begreppet funktionell nedbrytning. Beskriv varför och när vi vill göra
funktionell nedbrytning, och vad vi vill uppnå. Ge ett konkret exempel.
"""


""" Uppgift A6: 5p
Förklara begreppet gränssnitt, och hur vi bör förhålla oss till dessa.
"""


""" Uppgift A7: 4p
Förklara begreppen supertyp och subtyp, och hur de påverkar varandra.
"""

# Max poäng del A: 32p
# Krav för godkänt betyg: 24p


# ------- DEL B ------- #


def uppgiftB1():
    """ Uppgift B1: 6p
    Förklara noggrant vad som skrivs ut och varför det skrivs ut som det
    gör när följande kod körs:
    """
    z = Z("Run 1")
    z = Z("Run 2")

class X:
    def __init__(self, msg):
        print(msg)

class Y:
    x1 = X("Static in Y")

class Z:
    x1 = X("Static in Z")

    def __init__(self, msg):
        self.x2 = X("Instance in Z")
        self.b1 = Y()
        print("Z is done - " + msg)

uppgiftB1()


""" Uppgift B2: 4p
Förklara vad som menas med att listor har referens-semantik, medan tupler har
värde-semantik.
"""


""" Uppgift B3: 6p
Förklara vad en klass - dvs det vi deklarerar med hjälp av keyword class - är.
Beskriv samtliga aspekter av en klass, och ge exempel på hur vi kan använda oss
av dem.
"""

""" Uppgift B4: 6p
Förklara Principle of Least Astonishment, och vad den säger om hur vi bör
förhålla oss till funktioner, metoder, och deras argument.
"""


"""Uppgift B5: 6p
Presentera en algoritm för en funktion 

all_positive_submatrices(the_matrix: List[List[int]], size: int) 

som hittar och returnerar alla sub-matriser av storlek size*size,
vars sammanlagda värde på elementen i sub-matrisen är >0. 

Presentera ditt svar som ett eller flera flödesscheman, som pseudo-kod
("kodskiss"), eller som faktisk kod i valfritt (känt) programmeringsspråk.

Exempel på körning:
m1 = [[-1,-2,-3],
      [-3,-5, 6],
      [7, 8, 9]]
m2 = [[-1, -2, -3, -4],
      [ 5, 6, -7, -8],
      [-9, 10, -11, -12],
      [-13, 14, 15, -16]]

all_positive_submatrices(m1, 2)
[[[3, 5],[7, 8]], [[5, 6], [8, 9]]]

all_positive_submatrices(m2, 3)
[[[5, 6, -7], [-9, 10, -11], [-13, 14, 15]]] 

all_positive_submatrices(m1, 4)
[]

"""

# Max poäng del A+B: 60p
# Krav för betyg 4: 36p
# Krav för betyg 5: 48p
