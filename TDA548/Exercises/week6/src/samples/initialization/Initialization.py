# package samples.initialization

from C import C


# This is the process of initializing
# when inheritance and static is involved
#
# Order of initialization:
# - Any static initialization (for class) in written order
# - Any instance variable initialization in written order
# - Finally constructor (if inheritance call super class constructor first)
def initialization_program():
    print("Program starts")
    c = C(3, "Created in program")


if __name__ == "__main__":
    initialization_program()
