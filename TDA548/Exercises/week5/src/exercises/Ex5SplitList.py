# package exercises

# Partition a List into a number of sub lists with as equal length as possible
# NOTE: References may be shared
#
# See:
# - UseExceptions
def split_list_program():
    ints = [1, 2, 3, 4]

    ps = partition(ints, 2)
    print(ps[0] == [1, 2])
    print(ps[1] == [3, 4])

    ps = partition(ints, 4)
    print(ps[0] == [1])
    print(ps[1] == [2])
    print(ps[2] == [3])
    print(ps[3] == [4])

    # ps = partition(None, 3) # exception, list null or empty
    # ps = partition(ints, 5) # exception, list too short (n > len(ints))
    # ps = partition(ints, 0) # exception, n must be positive

    ints = [1, 2, 3, 4, 5]
    ps = partition(ints, 2)
    print(ps[0] == [1, 2])
    print(ps[1] == [3, 4, 5])

    ps = partition(ints, 3)
    print(ps[0] == [1])
    print(ps[1] == [2, 3])
    print(ps[2] == [4, 5])

    ints = [1, 2, 3, 4, 5, 6, 7]
    ps = partition(ints, 3)
    print(ps[0] == [1, 2])
    print(ps[1] == [3, 4])
    print(ps[2] == [5, 6, 7])


# --------- Methods -----------------------
def partition(the_list, nr_of_partitions):
    raise NotImplementedError
    # TODO implement


if __name__ == "__main__":
    split_list_program()
