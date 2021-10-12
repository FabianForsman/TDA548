# package samples.initialization

from X import X


class A:
    x = X("Class variable x in A")

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        print(f"Constructor A: i = {self.i}, j = {self.j}")
