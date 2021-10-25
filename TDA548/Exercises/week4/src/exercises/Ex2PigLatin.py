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
def to_pig_latin(str_to_translate) -> str:
    consonants_upper = "B C D F G J K L M N P Q S T V X Z H R W Y"
    consonants = consonants_upper + " " + consonants_upper.lower()
    sentance = ""
    char = ''
    for i in str_to_translate.split():
        for char in consonants:
            if i[0] == char:
                if i[1] == char and len(i) > 2:
                    if i[2] == char and len(i) > 3:
                        i = i[3:] + i[0] + "ay "
                        break
                    else:
                        i = i[2:] + i[0] + "ay "
                        break
                else:
                    i = i[1:] + i[0] + "ay "
                    break
        else:
            i = i + "way "
        sentance += i
    return sentance.strip()


def test():
    print(to_pig_latin("My name is Eric"))
    print(to_pig_latin("My name is Eric") == "yMay amenay isway Ericway")


if __name__ == "__main__":
    pig_latin_program()
