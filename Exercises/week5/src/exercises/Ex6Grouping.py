# package exercises

# Group a list of Positions into sub lists containing all Positions
# having the same row (so that we easily, given a row (int), can find all
# Positions that have the specified row)
# 
# See:
# - UseADict
def grouping_program():
    ps = generate_positions()
    print(ps)

    # Method will group all Points into list depending on row values
    # I.e. all Points with row = 2 in same list, etc.
    # Row is the key and the list containing all pair with row =2 is the value
    row_positions = group_by_row_value(ps)

    # Checking
    b = True
    for pos in row_positions[0]:
        b = b and (pos.row == 0)  # Testing
    print("All rows with 0: " + b)

    b = True
    for pos in row_positions[2]:
        b = b and (pos.row == 2)  # Testing
    print("All rows with 2: " + b)


# -------- Methods --------------------
# TODO
def group_by_row_value(list_of_pos):
    raise NotImplementedError


# Utility method, some "random" Points
# (0,-3), (0, -2) ... (0, 2)
# (1,-3), (1, -2) ... (1, 2)
# ...
def generate_positions():
    ps = []
    for i in range(3):
        for j in range(-3, 2):
            p = Position(i, j)
            ps.append(p)
    return ps


class Position:
    def __init__(self, i, j):
        self.row = i
        self.col = i

    def __str__(self):  # Get a nice printout (method called by print(ps)).
        return f"({self.row},{self.col})"


if __name__ == "__main__":
    grouping_program()
