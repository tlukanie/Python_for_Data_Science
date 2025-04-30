from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red
import cv2

def main():
	array = ft_load("landscape.jpg")

	inverted_image = ft_invert(array)
	red_image = ft_red(array)
	green_image = ft_green(array)
	blue_image = ft_blue(array)
	grey_image = ft_grey(array)
	print(ft_invert.__doc__)

	inverted_image_bgr = cv2.cvtColor(inverted_image, cv2.COLOR_RGB2BGR)
	red_image_bgr = cv2.cvtColor(red_image, cv2.COLOR_RGB2BGR)
	green_image_bgr = cv2.cvtColor(green_image, cv2.COLOR_RGB2BGR)
	blue_image_bgr = cv2.cvtColor(blue_image, cv2.COLOR_RGB2BGR)
	grey_image_bgr = cv2.cvtColor(grey_image, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", grey_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()