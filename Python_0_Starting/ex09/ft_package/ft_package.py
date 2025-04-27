def count_in_list(lst, word):
	counter = 0
	for el in lst:
		if el == word:
			counter += 1
	return counter