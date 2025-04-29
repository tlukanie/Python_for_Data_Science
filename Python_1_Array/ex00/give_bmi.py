# Add tests for edge cases
#BMI = weight / height^2

class TypeError(Exception):
	pass

class ListsNotOfTheSameSize(Exception):
	pass

def is_digit(nbr):
	'''Checks if number is digit or not and returns True or False'''
	try:
		int(nbr)
		return True
	except ValueError:
		return False

def is_float(nbr):
	'''Checks if number is float or not and returns True or False'''
	try:
		float(nbr)
		return True
	except ValueError:
		return False

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	'''Takes two lists with height and weight, calculates bmi and returns the results in form of list'''
	bmi = []
	bmi_result = 0
	if (len(height) != len(weight)):
		raise ListsNotOfTheSameSize("Error: passed lists are not of the same size")
	for hg,wg in zip(height, weight):
		try:
			if not (is_digit(hg) or is_float(hg)):
				raise ValueError(f"Invalid value: height={hg}")
			if not (is_digit(wg) or is_float(wg)):
				raise ValueError(f"Invalid value: weight={wg}")
			
			bmi_result = wg / hg**2
			bmi.append(bmi_result)
		except ValueError as e:
			print(e)
		except ZeroDivisionError:
			print(f"Error: Division by zero.")
	return	bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	'''Takes a list of bmi and limit integer and returns a list of Boolean results'''
	results = []
	el_flag = False
	try:
		if not is_digit(limit):
			raise ValueError("Error: Limit is not an integer")
		for el in bmi:
			if el < limit:
				el_flag = False
				results.append(el_flag)
			else:
				el_flag = True
				results.append(el_flag)
	except ValueError as e:
			print(e)
	return results