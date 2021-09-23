# package exercises


# Use a Stack to check parentheses (balanced and correct nesting)
# The parentheses are: (), [] and {}
#
# See:
# - UseAStack
# - UseString
# - SwitchStatement
def check_paren_program():
    # All should be true
    print(check_parentheses("()"))
    print(check_parentheses("(()())"))
    print(not check_parentheses("(()))"))  # Unbalanced
    print(not check_parentheses("((())"))  # Unbalanced

    print(check_parentheses("({})"))
    print(not check_parentheses("({)}"))  # Bad nesting
    print(check_parentheses("({} [()] ({}))"))
    print(not check_parentheses("({} [() ({)})"))  # Unbalanced and bad nesting


# ----------- Methods -------------------------
def check_parentheses(string):
    # TODO
    return False


def matching(string):
    paren_switcher = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    match = paren_switcher.get(string)
    if match is None:
        raise ValueError
    return match


if __name__ == "__main__":
    check_paren_program()
