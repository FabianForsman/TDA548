# package samples

# * String is a Java standard API to work with texts. A String is an immutable
# * object so you can't change the letters in a String, have to create a new String.
# *
# * You don't need to learn all the methods by heart,
# * if allowed to use on exam you'll get a list.
# *
# * Some usable String handling below (always avoid to reinvent the wheel)
def use_str_program():
    my_str = "abcdef"               # Will create an immutable str object

    # Compare strings
    print(my_str == "abcdef")       # str is a "primitive", use == for equality tests
    print(my_str is "absdef")       # This gives an error hint
    print(my_str != "qwerty")

    # Inspecting a string
    print(my_str.isspace())
    print(len(my_str))
    print(my_str[3])
    print(my_str[len(my_str) - 1])  # Last char!
    print(my_str[-1])               # Also last char!
    print(my_str[4:6])              # Slicing
    print(my_str[:4])               # From start to index 4
    print(my_str[-3:])              # From "three from the end" to end

    # # Updating a string - not possible, str is immutable!
    # my_str[0] = "q"       # TypeError: 'str' object does not support item assignment

    # Search inside a string
    my_str = "abcdefabcdef"
    print(my_str.find('a') == 0)
    print(my_str.find('X') == -1)       # Not found -1
    print(my_str.find("fab") == 5)      # Matches my_string
    print("cd" in my_str)               # in works for substrings
    print(my_str.startswith("abc"))
    print(my_str.endswith("def"))
    print(my_str.find("a", 3, 10) == 6) # find within a certain range
    print(my_str[3:10].find("a") == 6)  # same thing

    # Manipulate strings (will create new strings)
    my_str = "Success consists of going from failure"\
             + " to failure without loss of enthusiasm"

    print()
    print(my_str.upper()) # Creates a new string in upper case
    print(my_str)         # Original not changed

    my_str1 = my_str[0:4]  # Keep track of the new my_string
    print(my_str1)
    print(my_str1 != my_str)

    print("   abcde    ".strip() == "abcde")      # Remove leading/ending space
    print(my_str.replace("failure", "icecream"))
    print("abcdefaböab".replace("ab", "X"))

    # Convert to list and back
    str_as_list = list(my_str)
    print(str_as_list)
    my_str = "".join(str_as_list)
    print(my_str)

    # Work with a single char at the time
    for char in "1 2 hej 5":
        if char.isdigit():
            print(char)

    # Split into separate words
    my_strs = my_str.split()  # " " matches one space.
    for word in my_strs:
         print(word)

    # From primitive to String ...
    s1 = str(45)
    s2 = str(True)
    s3 = str(1.45)
    s4 = str("X")
    print(" ".join([s1, s2, s3, s4]))

    # From String to primitive
    i = int("678")
    f = float("4.57")
    b = bool("False")
    print(f"{i} {f} {b}")


if __name__ == "__main__":
    use_str_program()
