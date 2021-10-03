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
	print("Start of sjt_program")
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
def permutation_sjt(string) -> list[str]:
	arr = list(string)
	arr.sort()
	permutations: list = []
	d: int = -1 # Direction of the mobile number. -1 is descending, +1 is ascending
	arr = make_elems_mobile(arr, d)
	x = arr[-1][0] # The largest number which is the main to move. 
	y = arr[0][0] # The lowest number whish is the last to move.

	permutations.append(add_new_permutation(arr)) # Adds the first permutation (start-list).

	numbers: str = []
	for elem in arr:
		numbers.append(elem[0])
	# while(still_new_permutations(permutations) or len(permutations) == 1):
	for j in range(10):
		print("-----------------New ROUND-----------------")
		for i in reversed(numbers):
			for current_num in arr:
				if current_num[0] == i:
					num = current_num
			print(f"Element: {num} in start array: {arr}")
			is_mobile(arr, num, x)
			# print(f"Element: {num} in array: {arr}")
			new_permutation(permutations, arr)
			if not i == numbers[-1]:
				break
			else:
				while(is_mobile(arr, num, x)):
					new_permutation(permutations, arr)
					continue
	return permutations


def make_elems_mobile(arr: list[list], d):
	"""
	Returns list with elem and it's mobile direction, which is descending by default.
	"""
	arr_d = [] # List with direction.
	for elem in arr:
		arr_d.append([elem, d]) 
	return arr_d


def still_new_permutations(permutations: list) -> bool:
	return not permutations[-1] == permutations[0]


def new_permutation(permutations: list, arr: list):
	"""
	Appends a new permutation to the list.
	"""
	permutations.append(add_new_permutation(arr))


def swap(arr: list[list], val1: int, val2: int):
	"""
	Swaps 2 lists with each other.
	"""
	arr[val1], arr[val2] = arr[val2], arr[val1]


def is_mobile(arr: list[list], num: list, x: int):
	"""
	Checks if the current number can switch place with the adjacent number in it's direction. 
	"""
	direction = num[1]
	current_pos: int = arr.index(num)
	try:
		adjacent_num: list = arr[current_pos + direction]
	except:
		adjacent_num: list = arr[0]
	has_swapped: bool = False

	has_swapped = can_swap_with_adjacent(arr, num, adjacent_num, current_pos)
	stop_and_swap(arr, num, adjacent_num, current_pos, direction, x)
	print(f"has_swapped is {has_swapped}")
	return has_swapped


def can_swap_with_adjacent(arr: list[list], num: list, adj: list, num_to_swap: int):
	direction: int = num[1]
	current_pos: int = arr.index(num)
	print(f"Current: {num[0]}, Adjacent: {adj[0]}, Pos: {current_pos}")

	if num[0] > adj[0] and within_bounds(arr, num, direction):
		swap(arr, num_to_swap, num_to_swap + direction) # Swaps the number with the number in its direction.
		return True
	else:
		print("Can't swap!")
		return False # Does not append the current arr to permutations because no change was made. 

def within_bounds(arr: list[list], num: list, direction: int):
	"""
	Checks if the current number is at the edge of the list. If so, it has to stop.
	"""
	if arr.index(num) == len(arr) - 1 and direction == 1 or arr.index(num) == 0 and direction == -1:
		return False
	return True

def stop_and_swap(arr: list[list], num: list, adj: list, current_pos: int, direction: int, x: int):
	"""
	Checks if the currently moving number has to stop and change direction.
	"""
	if current_pos == 0 and num[0] > adj[0] and direction == -1:
		reverse_direction(arr, current_pos)
	elif current_pos == len(arr) - 1 and num[0] < adj[0] and direction == 1:
		reverse_direction(arr, current_pos)
	elif (current_pos == 0 or current_pos == len(arr) - 1) and num[0] == x:
		reverse_direction(arr, current_pos)
	else:
		print("Stopped but did not reverse direction!")

def reverse_direction(arr: list[list], current_pos: int):
	arr[current_pos][1] *= -1 # Swaps direction


def set_direction(arr: list[list], current_pos: int, direction: int):
	arr[current_pos][1] = direction


def add_new_permutation(arr_d: list) -> list:
	temp = []
	for elem in arr_d:
		temp.append(elem[0]) # Adds the number to a list and ignores the direction.
	return temp


if __name__ == "__main__":
	sjt_program()