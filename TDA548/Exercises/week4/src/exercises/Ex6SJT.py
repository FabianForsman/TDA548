# package exercises

# Using Steinhaus-Johnson-Trotter (non-recursive) algorithm for permutations
# See https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm
# 
# See:
# - UseString
# - UseAList
def sjt_program():
	# Call permutation method
	numbers = ""
	n: int = int(input("How many numbers? >"))
	if n == 0:
		return False

	nr_permutations = n
	for i in range(n):
		numbers += str(i + 1)
		if not i == 0:
			nr_permutations *= i

	perms = permutation_sjt(numbers)
	print("Start of sjt_program")
	for s in perms:
		print(s)
	print(f"Nr of permutations is {nr_permutations}: {len(perms) == nr_permutations}")
	# We should find the original value exactly once
	count = 0
	for s in perms:
		if s == numbers:
			count += 1
	print(f"Original exists once: {count == 1}")


# Steinhaus–Johnson–Trotter permutation algorithm iterative!
# Use functional decomposition!
# TODO
def permutation_sjt(string) -> list[str]:
	arr = string_to_arr(string)
	arr_size = len(arr)
	permutations = []
	add_new_permutation(permutations, arr)
	still_new_permutations = True
	while still_new_permutations:
		still_new_permutations = new_permutation(permutations, arr, arr_size)
	return permutations


def string_to_arr(string) -> list[list]:
	arr = list(string)
	arr.sort()
	return make_elems_mobile(arr)

def make_elems_mobile(arr: list) -> list[list]:
	"""
	Returns list with elem and it's mobile direction, which is descending by default.
	"""
	d = -1 # Default value of direction. -1 is descending, +1 is ascending.
	arr_d = [] # List with direction.
	for elem in arr:
		arr_d.append([elem, d]) 
	return arr_d

def search_for_mobile(arr: list, arr_size: int, mobile: int):
	for i in range(arr_size):
		if arr[i][0] == mobile:
			return i + 1


def find_largest_mobile(arr: list, arr_size: int) -> int:
	mobile_prev: 	str = "0"
	mobile: 		str = "0"
	for i in range(arr_size):
		if arr[i][1] == -1 and not i == 0:
			if arr[i][0] > arr[i - 1][0] and arr[i][0] > mobile_prev:
				mobile = arr[i][0]
				mobile_prev = mobile
		if arr[i][1] == 1 and not i == arr_size - 1:
			if arr[i][0] > arr[i + 1][0] and arr[i][0] > mobile_prev:
				mobile = arr[i][0]
				mobile_prev = mobile
	if mobile == "0" and mobile_prev == "0":
		return "0"
	else:
		return mobile


def new_permutation(permutations: list, arr: list, arr_size: int):
	mobile: str = find_largest_mobile(arr, arr_size)
	pos: int = search_for_mobile(arr, arr_size, mobile)
	try: 
		if arr[pos - 1][1] == -1:
			swap(arr, pos - 1, pos - 2)

		elif arr[pos - 1][1] == 1:
			swap(arr, pos, pos - 1)
	except:
		return False
	direction_change(arr, arr_size, mobile)
	add_new_permutation(permutations, arr)
	return True

def direction_change(arr: list, arr_size: int, mobile: int):
	"""
	Changes the direction of elements greater than largest mobile integer.
	"""
	for i in range(arr_size):
		if arr[i][0] > mobile:
			if arr[i][1] == 1:
				arr[i][1] = -1
			elif arr[i][1] == -1:
				arr[i][1] = 1


def add_new_permutation(permutations: list[str], arr: list):
	temp_list = ""
	for elem in arr:
		temp_list += elem[0]
	permutations.append(temp_list)


def swap(arr: list, val1, val2):
	arr[val1], arr[val2] = arr[val2], arr[val1]

if __name__ == "__main__":
	run: bool = True
	while run:
		run = sjt_program()