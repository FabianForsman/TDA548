# package exercises

#
#  Some puzzlers
#  General improvement of programming skills
#
#  See:
#  - LoopPuzzler
#
def puzzle_program():
    # TODO Write solution (for loops) directly here
    print("a)")
    x = 1
    for i in range(10):
        for j in range(10):
            print(f"{(j+1)*x} ", end = '')
            if (j+1)*x < 10:
                print(" ", end = '')
        print()
        x+=1
    
    print("\nb)")
    for i in range(10):
        print("X"*(10-i))
    
    print("\nc)")
    for i in range(10):
        print(" "*i + ("X"*10))

if __name__ == "__main__":
    puzzle_program()
