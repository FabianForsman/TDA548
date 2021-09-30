# package exercises
#
#  *   Extract numbers from strings
#  *
#  *   See:
#  *  - UseAList
#  *  - UseString
#  *  - Exceptions
def read_number_program():
	# Second argument (0) is index to start looking for digits.
	# Return value is index directly after last read digit
	numbers, stop_index = read_number("1", 0)
	print(stop_index == 1)
	# The number should be in the list numbers (method should add number to list)
	print(1 in numbers)

	numbers, stop_index = read_number("123", 0)
	print(stop_index == 3)
	print(123 in numbers and 1 not in numbers)

	numbers, stop_index = read_number("123abc", 0)
	print(stop_index == 3)
	print(123 in numbers)
	numbers, stop_index = read_number("12345abc", 0)
	print(stop_index == 5)
	print(12345 in numbers)
	numbers.clear()

	numbers, stop_index = read_number("abc123abc", 3)
	print(stop_index == 6)
	print(123 in numbers)

	# Empty string should not be accepted; raise exception
	try:
		numbers, stop_index = read_number("", 0)
	except ValueError as err:
		print(repr(err))


# ----------- Methods-----------------------------------
# First parameter is a list in which
def read_number(string_to_parse: str, start_index: int) -> tuple:
	# TODO
	numbers = "0123456789"
	return_num = ""
	stop_index = 0
	for elem in string_to_parse:
		if elem in numbers:
			return_num += elem
			stop_index += 1
	print(stop_index)
	return [int(return_num)], stop_index


def read_number2(string_to_parse: str, start_index: int):
	temp = []
	char_found = False
	string_to_parse = list(string_to_parse)
	string = ""
	for start_index in range(len(string_to_parse)):
		try:
			string_to_parse[start_index] = int(string_to_parse[start_index])
		except ValueError:
			# print("Found char!")
			char_found = True
		if not char_found:
			temp.append(int(string_to_parse[start_index]))
	for elem in temp:
		string += str(elem)
	return int(string), start_index + 1


if __name__ == "__main__":
	read_number_program()
