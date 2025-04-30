from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red


def main():
	array = ft_load("landscape.jpg")
	ft_invert(array)
	ft_red(array)
	ft_green(array)
	ft_blue(array)
	ft_grey(array)
	print(ft_invert.__doc__)


if __name__ == "__main__":
	main()