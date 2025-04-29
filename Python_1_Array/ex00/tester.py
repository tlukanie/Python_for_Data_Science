from give_bmi import give_bmi, apply_limit, ListsNotOfTheSameSize

def main():
	'''Main function to test the implemented functions'''
	try:
		height = [2.71, 1.15]
		weight = [165.3, 38.4]
		bmi = give_bmi(height, weight)
		print(bmi, type(bmi))
		print(apply_limit(bmi, 25))
	except ListsNotOfTheSameSize as e:
		print(e)
	except ValueError as e:
		print(e)

if __name__ == "__main__":
	main()