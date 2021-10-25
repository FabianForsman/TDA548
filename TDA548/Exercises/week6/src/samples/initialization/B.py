# package samples.initialization

from X import X
from A import A
# Cannot import C, that would cause a loop in static initialization
# from C import C


class B(A):
    # Cannot use C, that would cause a loop in initialization
    # c = C(4, "Class variable c in B")

    def __init__(self, i: int):
        super().__init__(i, 9)
        self.x = X("Instance variable x in B")
        print(f"Constructor B: {i}")
