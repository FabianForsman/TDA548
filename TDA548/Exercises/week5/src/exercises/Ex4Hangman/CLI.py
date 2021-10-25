# package exercises.ex4hangman

import os.path
from HangMan import Result
from FileService import *

# Command Line Interface for Hangman OO model
# No game logic allowed here, only player interaction
#
# Run this to run the game
#
# See
# - usemoreclasses/
# - UseExceptions
DEFAULT_PATH = os.path.join("words.txt")
NL = "\n"


def play_hangman_cli():
    try:
        the_word = get_random_word_from_file(DEFAULT_PATH)
    except IOError as ioe:
        plot_exception(ioe)
        exit(0)
    # TODO build OO model
    # TODO print welcome message
    # TODO implement game loop
    # TODO print win/loss message


# ------------- Helpers and graphics --------------------------
# Parts of the hanging man (NL is the new line character, don't need to understand)
parts = [
    "---|" + NL,
    "   |" + NL,
    "   O" + NL,
    "  /",
    "|",
    "\\" + NL,
    "  /",
    " \\" + NL,
]


def guess_character():
    while True:
        character = input("Enter a character > ")
        if len(character) == 1 and character.isalpha():
            break
    return character


def plot_mask(mask):
    for ch in mask:
        print(ch + " ")
    print()


def plot_man(health: int):
    for part in parts:
        print(part, end='')
    if health in [1, 3, 4]:  # Layout
        print()


def welcome_msg(word_length):
    print("Welcome to HangMan, try to guess the word! It's " +
          word_length + " characters long")


def win_msg(result, nr_guesses, answer):
    if result == Result.WIN:
        print(f"You made it. You needed {nr_guesses} tries.")
    else:
        print("Sorry you lost. Word(s) was: " + answer)


def plot_exception(e):
    print("Exception: " + str(e))


if __name__ == "__main__":
    play_hangman_cli()
