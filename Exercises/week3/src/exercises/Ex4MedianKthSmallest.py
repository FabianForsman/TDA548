# package exercises

#
# Even more list methods, possibly even trickier
#
def median_kth_smallest_program():
    list1 = [9, 3, 0, 1, 3, -2]

    print(not is_sorted(list1))  # Is sorted in increasing order? No not yet!

    sort(list1)     # Sort in increasing order, original order lost!

    print(list1 == [-2, 0, 1, 3, 3, 9])

    print(is_sorted(list1))  # Is sorted in increasing order? Yes!

    list2 = [5, 4, 2, 1, 7, 0, -1, -4, 12]
    list3 = [2, 3, 0, 1]
    print(median(list2) == 2)    # Calculate median of elements
    print(median(list3) == 1.5)

    list4 = [2, 3, 0, 1, 5, 4]
    list5 = [5, 4, 2, 2, 1, 7, 4, 0, -1, -4, 0, 0, 12]
    print(k_smallest(list4, 2) == 1)   # Second smallest is 1
    print(k_smallest(list5, 5) == 2)   # 5th smallest is 2

    # ---------- Write methods here --------------
def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True
        

def sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


def median(list):
    sort(list)
    if len(list) % 2 == 0:
       value1 = list[int((len(list)-1)/2)]
       value2 = list[round((len(list)-1)/2)]
       return (value1 + value2)/2
    else:
        return list[round(len(list)/2)]

def k_smallest(list, num):
    sort(list)
    list = remove_duplicates(list)
    return list[num-1]

def remove_duplicates(list):
    temp = []
    for i in list:
        if i not in temp:
            temp.append(i)
    return temp

if __name__ == "__main__":
    median_kth_smallest_program()
