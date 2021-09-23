# package exercises

# Using Steinhaus-Johnson-Trotter (non-recursive) algorithm for permutations
# See https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm
# 
# See:
# - UseString
# - UseAList
def sjt_program():
    # Call permutation method
    perms = permutation_sjt("123456")

    print(f"Nr of permutations is 720: {len(perms) == 720}")
    for s in perms:
        print(s)

    # We should find the original value exactly once
    count = 0
    for s in perms:
        if s == "123456":
            count += 1
    print(f"Original exists once: {count == 1}")


# Steinhaus–Johnson–Trotter permutation algorithm iterative!
# Use functional decomposition!
# TODO
def permutation_sjt(string):
    return []


if __name__ == "__main__":
    sjt_program()
