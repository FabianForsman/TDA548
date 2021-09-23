# package samples

# Error handling in Python is done through so called exceptions
# (same as in almost all modern languages (C is not modern...))
# We use special statements 'raise' and 'try-except' to work with
# exceptions in an orderly fashion, to prevent the program from
# crashing.
def exceptions_program():
    # Certain built-in operations lead to exceptions
    try:
        print(7 / 0)        # Integer division by zero is undefined
    except Exception:       # We say that we "catch" the exception
        print(f"Oops!")

    # Different errors lead to different types of exceptions,
    # all of them subtypes to Exception so the above except clause
    # will catch them all, but we can (and should) be more specific:
    try:
        print(7 / 0)
    except ZeroDivisionError:
        print("Oops!")

    my_list = [1, 2, 3]
    try:
        print(my_list[100])
    except IndexError:
        print("Oops!")

    # If we try to catch an exception of one type,
    # but a different one is raised, the except clause
    # won't run, and the exception is propagated.
    # Uncommenting will give an IndexError:
    # try:
    #     print(my_list[100])
    # except ZeroDivisionError:
    #     print("Oh-oh...")

    # We can have multiple except clauses, as well as
    # a 'finally' clause that always runs:
    try:
        print(my_list[100])
    except ZeroDivisionError:
        print("Oh-oh...")
    except IndexError:
        print("Oops!")
    finally:
        print("Phew!")

    # The finally clause runs even if no exception is raised:
    try:
        print(my_list[0] == 1)
    except IndexError:
        print("Oops!")
    finally:
        print("Phew!")

    # We can omit all except clauses if we have a finally clause (but uncaught
    # exceptions will then keep propagating.
    try:
        # print(my_list[100]) # Uncomment and the finally clause still happens, then crash
        print(my_list[0] == 1)
    finally:
        print("Yeah, this happened.")

    # An exception is an object, and we can bind it to a variable
    # to inspect it in the except clause:
    try:
        print(my_list[100])
    except IndexError as index_error:
        print(repr(index_error))
        print(index_error)
        print(type(index_error))

    # We can raise exceptions ourselves using the 'raise' statement
    try:
        raise ValueError('WTF?')
    except ValueError as wtf:
        print(repr(wtf))

    # We can create our own exception types, by inheriting an existing
    class MyOwnExceptionalException(BaseException):
        pass

    try:
        raise MyOwnExceptionalException('Woohoo!')
    except MyOwnExceptionalException as moee:
        print(repr(moee))

    # If a function raises an exception but doesn't catch it,
    # it becomes the caller's responsibility to catch it instead
    def crappy_function():
        raise MyOwnExceptionalException('Crappy!')

    try:
        crappy_function()
    except MyOwnExceptionalException as moee:
        print(repr(moee))


if __name__ == "__main__":
    exceptions_program()
