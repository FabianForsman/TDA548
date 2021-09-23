# package exercises

# A String problem
#
# See:
# - UseString
def string_ordering_program():
    # Yes, "aa bb cc" is ordered like "abc" because all
    # a's are before all b's that are before all c's
    print(is_ordered_like("abc", "aa bb cc"))
    # Yes, all a's before all b's
    print(is_ordered_like("ab", "aa eee bb ddd cc"))
    # Yes, all e's before all c's
    print(is_ordered_like("ec", "aa eee becb c dddc"))

    # Not all c's are before all b's
    print(not is_ordered_like("acb", "aa bb cc"))
    # Not all b's before all c's
    print(not is_ordered_like("abc", "aa bb ccc b"))
    # No!
    print(not is_ordered_like("bac", "aa eee bbb ddd ccc"))

    # Degenerate cases
    print(is_ordered_like("a", "aa bb cc"))
    print(is_ordered_like("", "aa bb cc"))
    print(is_ordered_like("abc", ""))
    print(not is_ordered_like("ax", "aa bb cc"))


# -------- Methods ---------------
# TODO
def is_ordered_like(ordering, list_to_test):
    pass


if __name__ == "__main__":
    string_ordering_program()
