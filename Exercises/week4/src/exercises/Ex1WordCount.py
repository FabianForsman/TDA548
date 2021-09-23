# package exercises

# Count number of words in some text
#
# See:
# - UseString
def word_count_program():
    print(count_words("") == 0)
    print(count_words("hello") == 1)
    print(count_words(" hello ") == 1)
    print(count_words("hello world") == 2)
    print(count_words("hello    world") == 2)
    print(count_words("   hello    world  ") == 2)
    s = "Education is what remains after one has forgotten what one has learned in school."
    print(count_words(s) == 14)


# --------------- Methods -----------------
# TODO
def count_words(string: str):
    return -1


if __name__ == "__main__":
    word_count_program()
