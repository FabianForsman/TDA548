# package samples.initialization

from B import B


class C(B):
    def __init__(self, i, string):
        super().__init__(i)
        print("Constructor C: " + string)

