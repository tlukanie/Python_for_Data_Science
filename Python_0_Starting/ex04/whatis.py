import sys

#len
def  arguments_nbr(input):
	num = 0
	for word in input:
		num += 1
	return num

#isdigit
# The `not in` operator in Python is used to check if an element 
# is **not present** in a sequence (like a string, list, tuple, or dictionary)
def check_is_nbr(input):
	digits = "0123456789"
	for char in input:
		if char not in digits:
			return False
	return True
				
if(arguments_nbr(sys.argv) > 2):
	print("AssertionError: more than one argument is provided")
	sys.exit(1)
elif(arguments_nbr(sys.argv) == 1):
	sys.exit(1)
else:
	input_string = sys.argv[1]

	if ((input_string[0] == '-' and check_is_nbr(input_string[1:])) or check_is_nbr(input_string)):
		nbr = int(input_string)
		if(nbr % 2 == 0):
			print("I'm Even")
		else:
			print("I'm Odd")
	elif (type(input_string) != int):
		print("AssertionError: argument is not an integer")
