# package exercises

# Pig Latin, silly secret language
# https://en.wikipedia.org/wiki/Pig_Latin
#
# See:
# - UseString
def pig_latin_program():
    input_str = input("Text to translate? >")
    print(to_pig_latin(input_str))


# ---------- Methods --------------------
# TODO
def to_pig_latin(str_to_translate) -> str:
    return ""


def test():
    print(to_pig_latin("My name is Eric") == "yMay amenay isway Ericway")


if __name__ == "__main__":
    pig_latin_program()
