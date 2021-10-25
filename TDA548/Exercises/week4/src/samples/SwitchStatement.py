# package samples

# A switch "statement" is a selection (like if) but only use equality (== or equals)
# to match. These exist as actual statements (like if, for, while) in some languages
# (Java, C#, C++, ...), but not in Python. It's easy to simulate though, and is a lot
# more compact than a long if-elif-elif-elif-...-else ...
from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1


def switch_statement_program():
    i = 4
    # Switch statement emulation
    int_switcher = {  # Build a switcher dictionary
        0: "match 0",
        1: "match 1",
        2: "match 2",
        3: "match 3",
        4: "match 4"
    }
    text_to_print = int_switcher.get(i, "no match")
    print(text_to_print)

    s = "qqq"
    str_switcher = {  # Switch with String
        "aaa": "match aaa",
        "bbb": "match bbb"
    }
    print(str_switcher.get(s, "no match"))  # Prints the default value

    c = Color.BLACK
    color_switcher = {  # Works well with enum
        Color.WHITE: "white",
        Color.BLACK: "black"
    }
    print(color_switcher.get(c, "no match"))

    zip_switcher = dict(zip(list(Color), ["white", "black"]))
    print(zip_switcher)
    print(zip_switcher.get(c))

    # We can build our dictionary using variables as keys.
    i, j, k = 0, 1, 2
    var_switcher = {
        j: 1,
        k: 2
    }
    print(var_switcher.get(i))  # None, if no other default is given


if __name__ == "__main__":
    switch_statement_program()
