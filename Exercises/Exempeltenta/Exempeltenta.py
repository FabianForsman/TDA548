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

Svar:
for-loopen körs ett specifierat antal gånger och används när man vet hur många gånger man vill utföra koden.
Den räknar igenom en lista vars element används (ofta, men inte alltid) till att göra något i koden.
while-loopen används när vi inte vet hur många gånger som koden ska exekveras.
Den koller om ett statement är sant eller falsk, och utför koden enligt detta.

for elem in my_list:
    do_something()

run = True
while run:
    if stop_running():
        run = False
"""


def uppgiftA2():
    """
    Uppgift A2: 4p
    Förklara noggrant steg för steg hur variabeln x får det värde som skrivs
    ut, och vilket värde.
    
    Svar:
    x skrivs ut efter att den yttre for-loopen har körts och därav skrivs endast ut en gång, med avseende på att vi
    inte vet vad utomstående koden gör.
    första loopen för a:
    a = 0
    b = 0
    x += 1 = 1
    b == 1 -> False

    x = 1!

    b ökar först eftersom forloopen som ligger lokalt i ett statement körs först, och när den är klar går vi vidare.
    a = 0
    b = 1
    x += 1 = 2
    b == 1 -> True
    break -> hoppar ut b-for-loopen och går vidare i a.

    a = 1
    b = 0
    x += 1 = 3
    b == 1 -> False

    som innan där b == 1 -> True
    x = 4

    a = 2
    b = 0
    - > x = 5

    a = 2
    b = 1
    - > x = 6

    a = 3 -> for-loopen är över då range(x) räknar från 0 till x - 1, d.v.s. körs så länge a < x

    Svar: x = 6
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

    Svar:
    Se bild.
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

Svar:
def as_set(in_list: list) -> list:
    temp_list: list = []
    for elem in in_list:
        if elem not in temp_list:
            temp_list.append(elem)
    temp_list.sort()
    return temp_list
"""


""" Uppgift A5: 4p
Förklara begreppet funktionell nedbrytning. Beskriv varför och när vi vill göra
funktionell nedbrytning, och vad vi vill uppnå. Ge ett konkret exempel.

Svar:
Funktionell nedbrytning innefattar att bryta upp koden till flera funktioner, istället för att ha allt i samma funktion, main etc.
Detta gör vi för att göra koden mycket mer läsbar och för att andra ska kunna använda våra funktioner.
Om det finns mycket kod som blir grötig kan det bli mycket bättre om den bryts ner till mindre delar. 
Det blir också bättre vid testning av koden, då specifika funktioner för specifika delar kan köras med
testkod för att se om helheten fungerar.

Det är dock viktigt att vi fortfarande följer command query principle, d.v.s. att funktionen antingen fungerar som ett kommando,
alltså att den har en effekt eller att den ska kunna bli "frågan en fråga" och åstadkomma ett resultat, d.v.s. returnera ett värde.
Att ställa en fråga ska inte påverka svaret!

Ett konkret exempel är just felhantering. Istället för att ha all felhantering ett och samma block delar vi upp
varje fel med en funktion, vilket gör det mycket mer läsbart och det blir lättare att se vad som blir fel.

"""


""" Uppgift A6: 5p
Förklara begreppet gränssnitt, och hur vi bör förhålla oss till dessa.
Gränssnitt är det som är synligt till anroparen, d.v.s. det vi vill visa. Detta inkulderar publika metoder, attribut och docstrings etc.
När användaren skriver ex. en instans från en klass:s namn med punkt-operatorn efter kommer funktion, metod och attributs- gränsnittet upp.
Detta används för att visa vad användaren kan göra med klassen.

Svar:
Vid användandet av funktioner är docstrings bra, eftersom det är en beskrivning av vad funktionen ska göra. 
skrivs mha 
"""
"""

Vi bör vara tydliga i gränssnittet med vad koden ska åstadkomma så att det blir så lätt för användaren som möjligt. Det ska vara
tydligt vad en funktion ska göra, d.v.s. vi ska utnyttja principle of least astonishment. 
"""


""" Uppgift A7: 4p
Förklara begreppen supertyp och subtyp, och hur de påverkar varandra.

Svar:
supertyp och subtyp handlar om arv. En subtyp ärver av sin supertyp, vilket gäller generellt. Ett exempel är vid
superklasser och subklasser.

Att ha en superklass Pet är bra då alla husdjur, oavsätt vilket djur, har många gemensamma attribut och kan göra samma saker.
Antag att det finns en subklass Dog och Cat. Dessa kanske båda har ett namn och en ålder. Därav skapar vi detta i superklassen som de båda ärver av
eftersom det blir mer överskådlig och lättläst kod samt färre rader. Om något ändras i supertypen ändras det också i subtyperna, men inte tvärt om.
supertypen ärver inte av subtypen.
"""

# Max poäng del A: 32p
# Krav för godkänt betyg: 24p


# ------- DEL B ------- #


def uppgiftB1():
    """ Uppgift B1: 6p
    Förklara noggrant vad som skrivs ut och varför det skrivs ut som det
    gör när följande kod körs:

    Svar:
    X tar in en en parameter i konstruktiorn, en sträng, som print:ar denna parameter.

    När python hittar en klass med ett klassattribut som anropar en funktion för att få sitt värde
    kommer den funktoinen köras innan vi når if __name__ == "__main__":

    Först hittas Class X:
    Utför expression x1 = X("Static in Y")

    x1 är en instans av klassen X. X:s konstruktor anropas och därav printas parametern som skickas

    Sedna hittas Class Y:
    Utför expression x1 = X("Static in Z")

    x1 är en instans av klassen X. X:s konstruktor anropas och därav printas parametern som skickas

    z = Z("Run 1")
    Skapar ett objekt av klassen Z. Konstruktorn anropas.
    x1 är redan initerad och därav utförs inte igen eftersom det inte ligger i konstruktorn!

    z.x2 = X("Instance in Z")
    print:ar parametern.

    z.b1 = Y()
    Klassen Y:s konstruktor har vi inte override:at så den gör endast det en vanlig icke-hand-definerad konstruktor gör, skapar ett nytt objekt av klassens typ. 

    print-meddelande Z is done - " + msg, msg = "Run 1"

    z = Z("Run 1")
    override:ar z med ett nytt objekt där "Run 2" skickas. Samma som innan.

    Console print in order:
    Static in Y
    Static in Z
    Instance in Z
    Z is done - Run 1
    Instance in Z
    Z is done - Run 2

    
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

Svar:
referens-semantik, d.v.s. att elementet har en adress som pekar på heap:en där des värde ligger.
Listor är av godtycklig storlek, d.v.s. deras storlek går att ändra på efter initering (med append, pop etc.) Deras storlek går att ändra på efter initering.

Tupler å andra sidan är som en lista där elementen är omuterbara och detta är även dess storlek. Varje element i tuple:n har ett värde,
och detta går inte att ändra på. Det går inte att append:a till en tuple etc. Det som ligger i varje plats är ett värde, inte en referens till ett värde som det är i listor.
"""


""" Uppgift B3: 6p
Förklara vad en klass - dvs det vi deklarerar med hjälp av keyword class - är.
Beskriv samtliga aspekter av en klass, och ge exempel på hur vi kan använda oss
av dem.

Svar:
En klass är som en maskin som skapar objekt. Den skapar en egen type, vilker är klassen själv. Alla klasser i sig har också en övertyp (supertype) av typen type. 
Klasser i sig är ju också objekt, och alla objekt har en typ. 
I klassen hittar vi en ritning hur dess objekt ska se ut. När klassen anropas, och så länge det inte är en statisk klass med endast statiska metoder @staticmethod
skapas en ny instans av klassen med hjälp av konstruktorn, och därav ett objekt. 

Vid deklarationen av en klass C åstadkommer vi många saker på en och samms gång.
1. Vi deklarerar en *typ* C, för instanser av klassen.
2. Vi definerar ett *klassobjekt* med namn C och typen "type" och anger dess
implementation genom klassmetoder (statiska metoder) och klassattribut.
3. Vi ger en implementation av hur *instanser* av klassen uppfyller typen C
(och supertyper till C), genom instansmetoder och instansattribut. 
4. Vi beskriver, genom implementation av en *konstruktor* hur instanser av
klassen C skapas och initeras i klassobjektet C.

Att punk 1 och 3 är separata kan vi se genom att abstrakta metoder ingår i 1 men inte i 3.
Vi kan också se det genom att subtyper till C kan ge en alternativ implementaion (3),
men inte ändra typen (2)

Det finns alltid en klassdeklaration
Det finns alltid en definition av C då vi alltid skapar ett klassobjekt
när python kör igenom koden innan vi kommer till if __name__ == "__main__":
Det behöver inte finnas instansmetoder och instansattribut om klassen är abstrakt.
Det behövs inte finnas en egenskriven konstruktor, klassdefinitionen skaper det åt oss.
Om man aldrig ska skapa instanser av klassen behövs inte implementationen av en egen konstruktor.

"""

""" Uppgift B4: 6p
Förklara Principle of Least Astonishment, och vad den säger om hur vi bör
förhålla oss till funktioner, metoder, och deras argument.

Svar:
PoLA:s huvudmål är att vi bör implementera funktioner på ett sätt som leder till
minsta möjliga förvirring. Konkret finns det en uppsättning tumregler:
* Namngivning ska vara tydlig och korrekt.
* Metoder bör inte både utföra en effekt och returnera ett värde (Command query principle)
  Om något ska det delas upp i olika funktioner, d.v.s. utnyttja PoLA.
* Metoder bör inte uppdatera sina explicita argument om dessa är pass-by-reference.
  Du ska inte behöva oroa dig över ändrad data bara för att du skickar in det i en funktion.
* Metoder får uppdatera sina implicita argument som har pass-by-reference-semantik by default.
  exempelvis self vid instansmetoder. 
* Om du skulle bryta mot CQP eller att uppdatera sina explicita argument måste det
  vara väl dokumenterat varför och hur du bryter dem.
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
def all_positive_submatrices(the_matrix: list[list[int]], size: int) -> list:
    validate_arguments(the_matrix, size)
    return add_all_positive(the_matrix, size)

def add_all_positive(the_matrix: list[list[int]], size: int) -> list:
    nr_subs_height, nr_subs_width = determine_nr_of_subs(the_matrix, size)
    result = []
    for i in range(nr_subs_height):
        for j in range(nr_subs_width):
            sub_matrix = get_sub_matrix(the_matrix, i, j, size)
            add_if_positive(result, sub_matrix)
    return result

def add_if_positive(result, sub_matrix):
    if sum_matrix(sub_matrix) > 0:
        result.append(sub_matrix)

# Matrix helper functions
def determine_nr_of_subs(the_matrix, size):
    height, width = get_height_and_width(the_matrix)
    nr_subs_height = max(0, height - size + 1)  # if size is larger than height or width,
    nr_subs_width  = max(0, width  - size + 1)  # the task will be impossible
    print(f"Height: {nr_subs_height}, width: {nr_subs_width}")
    return nr_subs_height, nr_subs_width

def get_sub_matrix(the_matrix, start_row, start_col, size):
    return [row[start_col:start_col + size]
                for row in the_matrix[start_row:start_row + size]]

def sum_matrix(matrix_to_sum):
    return sum(map(sum, matrix_to_sum))

def get_height_and_width(the_matrix):
    height = len(the_matrix)
    width = 0 if height == 0 else len(the_matrix[0])
    return height, width

# Validating arguments
def validate_arguments(the_matrix: list[list], size: int):
    validate_size_argument(size)
    validate_matrix_argument(the_matrix)

def validate_size_argument(size: int):
    if size <= 0:
        raise ValueError("all_positive_submatrices: size must be positive: " + str(size))

def validate_matrix_argument(the_matrix: list[list[int]]):
    if not all_rows_have_same_size(the_matrix):
        raise ValueError("all_positive_submatrices: The matrix must be a proper NxM matrix")

def all_rows_have_same_size(the_matrix: list[list[int]]) -> bool:
    for row in the_matrix:
        if not len(the_matrix[0]) == len(row):
            return False
    return True


def uppgiftB5():
    m1 = [[-1,-2,-3],
      [-3,-5, 6],
      [7, 8, 9]]
    m2 = [[-1, -2, -3, -4],
      [ 5, 6, -7, -8],
      [-9, 10, -11, -12],
      [-13, 14, 15, -16]] 
    print(all_positive_submatrices(m1, 2))
    # [[[-3, -5],[7, 8]], [[-5, 6], [8, 9]]]

    print(all_positive_submatrices(m2, 3))
    # [[[5, 6, -7], [-9, 10, -11], [-13, 14, 15]]] 

    print(all_positive_submatrices(m1, 4))
    # []

    print(all_positive_submatrices(m2, 2))
# Max poäng del A+B: 60p
# Krav för betyg 4: 36p
# Krav för betyg 5: 48p

uppgiftB5()