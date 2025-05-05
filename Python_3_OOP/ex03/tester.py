from ft_calculator import calculator

def main():
	try:
		v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
		v1 + 5
		# print(v1.value)
		print("---")
		v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
		v2 * 5
		# print(v2.value)
		print("---")
		v3 = calculator([10.0, 15.0, 20.0])
		v3 - 5
		# print(v3.value)
		v3 / 5
		# print(v3.value)
	except TypeError as e:
		print(f"Error: {e}")
	except ZeroDivisionError as e:
		print(f"Error: {e}")
	except Exception as e:
		print(f"Unexpected error: {e}")


if __name__ == "__main__":
	main()