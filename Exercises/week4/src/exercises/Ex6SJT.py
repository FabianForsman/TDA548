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
def permutation_sjt(string) -> list[int]:
	arr = list(string)
	arr = [int(x) for x in arr]
	permutations: list = []
	x: int = arr[-1] # The last element which will be the one to move around.
	prev_index = first_permutations(permutations, arr, x)

	while still_new_permutations(permutations):
		current_index = arr.index(x)
		prev_index = swap(permutations, arr, x, prev_index, current_index)
	return permutations

def first_permutations(permutations: list, arr: list, x: int):
	permutations.append(new_permutation(arr))
	prev_index: int = arr.index(x)
	arr[-1], arr[-2] = arr[-2], arr[-1]
	permutations.append(new_permutation(arr))
	return prev_index

def still_new_permutations(permutations: list):
	return not permutations[-1] == permutations[0]

def swap(permutations: list, arr: list, x: int, prev_index: int, current_index: int):
	print(current_index, prev_index, end="")
	print(" -- ", end="")
	print(arr[0], arr[-1])
	if not arr[0] == x and not arr[-1] == x:
		if prev_index > current_index:
			arr[current_index], arr[current_index-1] = arr[current_index-1], arr[current_index]
			prev_index -= 1
		elif prev_index < current_index:
			arr[current_index], arr[current_index+1] = arr[current_index+1], arr[current_index]
			prev_index += 1
		else:
			print("Something went wrong")
			print(permutations)
			exit(0)
	else:
		if prev_index > current_index:
			print(arr[-2], arr[-1])
			arr[-1], arr[-2] = arr[-2], arr[-1]
			prev_index = -1 # restart to go up
		elif prev_index < current_index:
			arr[0], arr[1] = arr[1], arr[0]
			prev_index = len(arr) # restart to go down
		else:
			print("Something went wrong (2)")
			print(permutations)
			exit(0)
	permutations.append(new_permutation(arr))
	return prev_index

def new_permutation(arr: list):
	temp = []
	for elem in arr:
		temp.append(elem)
	return temp

if __name__ == "__main__":
	sjt_program()
