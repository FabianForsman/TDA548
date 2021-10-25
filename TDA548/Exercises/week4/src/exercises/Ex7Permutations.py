# package exercises

# Permutations of strings
#
# Implement using recursion:
# https://introcs.cs.princeton.edu/java/23recursion/
# https://en.wikipedia.org/wiki/Recursion_(computer_science)
#
# See:
# - UseString
# - UseAList
def permutations_program():
    ps = ["abc", "acb", "bac", "bca", "cab", "cba"]
    perms = permutations("abc")

    # Some checks
    print(len(perms) == 6)
    print(ps in perms)
    print("aab" not in perms)
    print("abb" not in perms)


# -------- Methods -----------
# TODO
def permutations(some_string: str):
    return [some_string]


if __name__ == "__main__":
    permutations_program()
