# package samples

def use_a_list_program():
    # Below we use a variable of an interface type (list)
    # We prefer variables of interface type because then we can change the implementation
    # without changing the rest of the program (not applicable here, but in general)
    the_list = []

    print(f"Length: {len(the_list)}")

    the_list.append(100)                # append last in the_list
    the_list.append(200)
    the_list.append(300)
    print(the_list)                     # List has a str method, easy to print out
    print(f"Length is 3: {len(the_list) == 3}")
    print(f"Value at index 2: {the_list[2]}")
    print(f"Index of 300 is 2: {the_list.index(300) == 2}")

    the_list.insert(0, 500)             # Will push other elements right
    print(f"100 is now at index 1: {the_list.index(100) == 1}")
    print(the_list)

    the_list.insert(50, 555)            # Index 50 doesn't exist, put it at the end.
    print(the_list)

    i = the_list.pop(1)                 # Remove using index
    print(the_list)
    print(f"Popped element was 100: {i == 100}")                     # element at index 1

    the_list.remove(200)                # Remove using value
    print(the_list)
    print(f"200 not in list: {200 not in the_list}")
    # the_list.remove(200)                # ValueError - value to remove must exist in list
    the_list.insert(1, 200)

    l2 = the_list[1:3]          # Creates a new list with the slice
    print(l2)
    the_list.insert(1, 400)     # Update original
    print(l2)                   # Slice unchanged, not the same list as the_list

    # ----- Traversing  ----------------------

    for elem in the_list:
        print(elem, end=" ")
    print()  # new line

    for i in range(len(the_list)):      # Same as previous, just clumsier...
        print(the_list[i], end=" ")
    print()  # new line

    for i in range(len(the_list)):      # ... but with access to the index,
        the_list[i] += 1                # we can also do indexed updates
    print(the_list)

    for elem in the_list:               # Without the index, we can still remove
        if elem > 200:                  # But really strange things happen when we do!
            the_list.remove(elem)
    print(f"Why isn't this list empty?: {the_list}")  # Can you figure out why the list isn't empty here?

    the_list.extend(l2)                 # Add a list onto a list
    print(the_list)

    # --- Clear a List  -----------------
    the_list.clear()
    print(f"List is now empty: {len(the_list) == 0}")

    # print(the_list[0]])   # Exception


if __name__ == "__main__":
    use_a_list_program()
