import numpy as np

class ListsOfDifferentSize(Exception):
	pass

def is_digit(nbr):
	'''Checks if number is digit or not and returns True or False'''
	try:
		int(nbr)
		return True
	except ValueError:
		return False

def slice_me(family: list, start: int, end: int) -> list:
	row_lengths = [len(row) for row in family]
	if (len(set(row_lengths)) > 1):
		raise ListsOfDifferentSize("Error: rows have diffierent number of columns.")
	if (type(family).__name__ != "list"):
		raise ValueError("Error: input passed is not a list.")
	if not is_digit(start):
		raise ValueError("Error: starting value is not an integer.")
	if not is_digit(end):
		raise ValueError("Error: ending value is not an integer.")
	new_family = np.array(family)
	rows_nbr = len(family)
	columns_nbr = len(family[0])
	print(f"My shape is : ({rows_nbr}, {columns_nbr})")
	result = new_family[start:end]
	print(f"My new shape is : ({len(result)}, {len(result[0])})")
	return (result.tolist())