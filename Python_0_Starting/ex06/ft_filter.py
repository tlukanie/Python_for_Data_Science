num_list = [1, 3, 5, 8, 22, 33]

def even_odd(num):
	if num % 2 == 0:
		return True
	else:
		return False

def add_sum(num):
	return num + 5

# MAKE LIST COMPREHENSIONS

def ft_filter(external_ft, data):
	'''ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
	if external_ft is None:
		for el in data:
			yield el
	else:
		for el in data:
			if external_ft(el) == True:
				yield el
			elif external_ft(el) == False:
				pass
			else:
				yield el

#evens_odds = filter(even_odd, num_list)

new_filter = ft_filter(add_sum, num_list)

# print(next(new_filter))
# print(next(new_filter))
for k in new_filter:
	print(k)
