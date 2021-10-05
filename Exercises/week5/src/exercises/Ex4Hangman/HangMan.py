# package exercises.ex4hangman

#  The Hangman game (in a text version)
#  This is the game logic
#
#  This illustrated the concept of an "OO-model" (i.e. many connected
#  objects from different classes). Objects working together to solve a problem.
from enum import Enum, auto

from Secret import Secret  # From the *file* Secret, import the *class name* Secret
from Man import Man


class Result(Enum):
    NONE = auto()
    WIN = auto()
    LOSE = auto()


class HangMan:
    def __init__(self, man: Man, secret: Secret):
        self.__man = man        # Other object in model
        self.__secret = secret  # Other object in model
        self.__nr_guesses = 0
        self.__result = Result.NONE

    # The game logic
    def update(self, ch: str):
        # TODO implement logic
        pass

    # ----- Getters used by CLI ------------------------
    def get_nr_of_guesses(self) -> int:
        return self.__nr_guesses

    def get_result(self):
        return self.__result

    # TODO More here
