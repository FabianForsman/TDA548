# package samples

# Using exceptions properly is not trivial, there are plenty of ground rules to adhere to.
def exceptions_test():
    # Assertions are special statements that can be used to
    # raise exceptions, to help us find bugs in our own code.
    assert 1 == 1       # This won't do anything, the expression is True
    # assert 1 == 0     # AssertionError, the expression is False

    assert not Fibonacci.is_cached(6)
    print(Fibonacci.get(7))
    assert Fibonacci.is_cached(6)
    assert Fibonacci.is_cached(7)
    # assert Fibonacci.is_cached(8)     # Will not be true
    assert not Fibonacci.is_cached(8)
    print("All basic assertions passed!")

    try:
        assert Fibonacci.is_cached(100)  # Will not be true
    except AssertionError:
        print("Oops - we never actually want to catch these, that would hide bugs!")

    try:
        Fibonacci.is_cached(-1)
    except ValueError as ve:
        print(ve)
        print("We shouldn't catch this either; calling a method with unacceptable arguments is also a bug!")

    print()
    # We've defined a so called "docstring" for our 'get' function;
    # we can inspect it using the builtin 'help' function
    help(Fibonacci.get)  # Note the lack of () - we're not calling the 'get' method.


class Fibonacci:
    __CACHE = {1: 1, 2: 1}
    __CACHE_TO = 2

    def __init__(self):
        raise NotImplementedError  # We don't want instances

    @staticmethod
    def get(n: int):
        """Calculates the nth value in the fibonacci sequence, in linear time.

        :param n: The ordinal number of the value in the fibonacci sequence,
                  must be greater than zero
        :type n: int

        :returns: The nth value in the fibonacci sequence
        :rtype: int

        :raises ValueError: If the argument for n is not greater than zero.
        """
        if n < 1:
            # We should always check that arguments passed to the function
            # are acceptable, before doing anything with them.
            # If not acceptable, it's a bug in the caller's code, not ours
            # Hence we shouldn't use assert, but instead raise an exception
            raise ValueError("Fibonacci.get: argument n must be positive")
        assert n >= 1  # We shouldn't get here unless this is true
        if n > Fibonacci.__CACHE_TO:             # We need to increase the cache
            Fibonacci.__calculate_and_cache(n)
        result = Fibonacci.__CACHE.get(n)
        # We should have a value in the cache - if not, it's a bug in our own code
        assert result is not None
        return result

    @staticmethod
    def __calculate_and_cache(n):
        for i in range(Fibonacci.__CACHE_TO, n):
            Fibonacci.__CACHE_TO += 1
            # Using 'get', we get a None if the key is not in the cache...
            x = Fibonacci.__CACHE.get(Fibonacci.__CACHE_TO - 1)
            # ... so we can use an assertion on the value
            assert x is not None
            # Using indexing instead, we wouldn't get None but a KeyError
            y = Fibonacci.__CACHE[Fibonacci.__CACHE_TO - 2]
            # No point asserting here, we've already gotten a KeyError signaling
            # any potential bugs in finding y
            Fibonacci.__CACHE[Fibonacci.__CACHE_TO] = x + y

    @staticmethod
    def is_cached(n):
        if n < 1:
            raise ValueError("Fibonacci.is_cached: argument n must be positive")
        b = n <= Fibonacci.__CACHE_TO
        assert not b or Fibonacci.__CACHE.get(n) is not None
        return b


if __name__ == "__main__":
    exceptions_test()
