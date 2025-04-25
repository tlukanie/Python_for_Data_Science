import sys

def arguments_nbr(input):
	'''Function that takes a string as input and returns number 
	of words in this string.'''
	num = 0
	for word in input:
		num += 1
	return num

class NonEncodable(Exception):
	pass

class BadArguments(Exception):
	pass

def morse_encoder(input):
	'''takes a string and converts it to Morse Code, displaying it 
	to the terminal. Returns nothing.'''
	MORSE_DICT = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}
	encodable_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
	for char in input:
		if char.upper() not in encodable_chars:
			raise NonEncodable("AssertionError: the arguments are bad")
	for char in input:
		if char.upper() in encodable_chars:
			print(MORSE_DICT[char.upper()], end="")
	print()

def main():
	'''Main function that handles exceptions and all the tests, processes 
	user input'''
	try:
		if(arguments_nbr(sys.argv) == 2):
			morse_encoder(sys.argv[1])
		else:
			raise BadArguments("AssertionError: the arguments are bad")
	except BadArguments as e:
		print(e)
		sys.exit(1)
	except NonEncodable as e:
		print(e)
		sys.exit(1)
	except KeyboardInterrupt:
		print("\nYou pressed CTRL + C")
	except Exception as e:
		print(f"Caught an unexpected error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()