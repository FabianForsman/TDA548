# package exercises

# A String problem
#
# See:
# - UseString
def string_ordering_program():
	# Yes, "aa bb cc" is ordered like "abc" because all
	# a's are before all b's that are before all c's
	print(is_ordered_like("abc", "aa bb cc"))
	# Yes, all a's before all b's
	print(is_ordered_like("ab", "aa eee bb ddd cc"))
	# Yes, all e's before all c's
	print(is_ordered_like("ec", "aa eee becb c dddc"))

	# Not all c's are before all b's
	print(not is_ordered_like("acb", "aa bb cc"))
	# Not all b's before all c's
	print(not is_ordered_like("abc", "aa bb ccc b"))
	# No!
	print(not is_ordered_like("bac", "aa eee bbb ddd ccc"))

	# Degenerate cases
	print(is_ordered_like("a", "aa bb cc"))
	print(is_ordered_like("", "aa bb cc"))
	print(is_ordered_like("abc", ""))
	print(not is_ordered_like("ax", "aa bb cc"))


# -------- Methods ---------------
# TODO
def is_ordered_like(ordering: str, list_to_test: str) -> bool:
	ordering = list(ordering)
	list_to_test = remove_spaces(list_to_test)
	temp_list = []
	index_list = []
	if len(list_to_test) == 0:
		return True
	for i in reversed(list_to_test):
		if i not in temp_list:
			temp_list.insert(0, i)
	for i in ordering:
		if i in temp_list:
			index_list.append(temp_list.index(i))
		else:
			return False
	if index_list == sorted(index_list):
		return True
	return False

def remove_spaces(list_to_test: str) -> list:
	list_to_test = list(list_to_test)
	for i in list_to_test:
		if i == " ":
			list_to_test.remove(i)
	return list_to_test

if __name__ == "__main__":
	string_ordering_program()
