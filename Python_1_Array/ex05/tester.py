from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red

def main():

	try:
		array = ft_load("landscape.jpg")
	except Exception as e:
		print(f"Error loading image: {e}")
		return
	try:
		ft_invert(array)
		ft_red(array)
		ft_green(array)
		ft_blue(array)
		ft_grey(array)
	except Exception as e:
		print(f"Error applying one of the filters: {e}")
		print(ft_invert.__doc__)

if __name__ == "__main__":
	main()