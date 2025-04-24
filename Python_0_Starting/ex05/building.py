import sys

def arguments_nbr(input):
	'''Function that takes a string as input and returns number of words in this string.'''
	num = 0
	for word in input:
		num += 1
	return num

def upper_letters_counter(input):
	'''Function that counts and returns number of Upper Letters in the provided string'''
	upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	counter = 0
	for char in input:
		if char in upper_alphabet:
			counter += 1
	return counter

def lower_letters_counter(input):
	'''Function that counts and returns number of Lower Letters in the provided string'''
	lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
	counter = 0
	for char in input:
		if char in lower_alphabet:
			counter += 1
	return counter

def punctuation_marks_counter(input):
	'''Function that counts and returns number of Punctuation Marks in the provided string'''
	punct_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	counter = 0
	for char in input:
		if char in punct_marks:
			counter += 1
	return counter

def spaces_counter(input):
	'''Function that counts and returns number of spaces in the provided string'''
	space = " "
	counter = 0
	for char in input:
		if char == space:
			counter += 1
	return counter

def digits_counter(input):
	'''Function that counts and returns number of digits in the provided string'''
	digits = "0123456789"
	counter = 0
	for char in input:
		if char in digits:
			counter += 1
	return counter

def display_results(input):
	'''Function that counts all the characters and prints the total amount and number of characters of each type separately in the provided string'''
	up_l = upper_letters_counter(input)
	ll = lower_letters_counter(input)
	pm = punctuation_marks_counter(input)
	sp = spaces_counter(input)
	dc = digits_counter(input)
	total = up_l + ll + pm + sp + dc
	print(f"The text contains {total} characters:")
	print(f"{up_l} upper letters")
	print(f"{ll} lower letters")
	print(f"{pm} punctuation marks")
	print(f"{sp} spaces")
	print(f"{dc} digits")

class TooManyArgumentsError(Exception):
    pass

def main():
	'''Main function that handles exceptions and all the tests, processes user input'''
	try:
		if(arguments_nbr(sys.argv) > 2):
			raise TooManyArgumentsError("AssertionError: more than one argument is provided")
			sys.exit(1)
		elif(arguments_nbr(sys.argv) == 1):
			print("What is the text to count?")
			input_string = input()
			display_results(input_string)
		else:
			input_1 = sys.argv[1]
			display_results(input_1)
	except TooManyArgumentsError as e:
		print(e)
		sys.exit(1)
	except KeyboardInterrupt:
		print("\nYou pressed CTRL + C")
	except Exception as e:
		print(f"Caught an unexpected error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
