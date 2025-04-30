from load_image import ft_load
import sys


def main():
	try:
		print(ft_load("landscape.jpg"))
	except Exception as e:
		print(e)
		sys.exit(1)


if __name__ == "__main__":
	main()