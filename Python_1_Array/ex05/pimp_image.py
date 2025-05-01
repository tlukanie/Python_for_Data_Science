import numpy as np
import cv2

def ft_invert(array) -> np.ndarray:
	'''Inverts the color of the image received.'''
	inverted_array = 255 - array 
	inverted_image_bgr = cv2.cvtColor(inverted_array, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", inverted_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()
	return inverted_array

def ft_red(array) -> np.ndarray:
	'''Makes the image recieved red colored.'''
	red_array = array.copy()
	red_array[:, :, 1] = 0 #vectorized operation
	red_array[:, :, 2] = 0
	red_image_bgr = cv2.cvtColor(red_array, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", red_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()
	return red_array


def ft_green(array) -> np.ndarray:
	'''Makes the image recieved green colored.'''
	green_array = array.copy()
	green_array[:, :, 0] = 0
	green_array[:, :, 2] = 0
	green_image_bgr = cv2.cvtColor(green_array, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", green_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()
	return green_array


def ft_blue(array) -> np.ndarray:
	'''Makes the image recieved blue colored.'''
	blue_array = array.copy()
	blue_array[:, :, 0] = 0
	blue_array[:, :, 1] = 1
	blue_image_bgr = cv2.cvtColor(blue_array, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", blue_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()
	return blue_array


def ft_grey(array) -> np.ndarray:
	'''Makes the image recieved grey colored.'''
	grey_array = array.copy()
	grey_intensity = grey_array[:, :, 0] / 3
	grey_intensity = grey_intensity + grey_array[:, :, 1] / 3
	grey_intensity = grey_intensity + grey_array[:, :, 2] / 3
    
	grey_array[:, :, 0] = grey_intensity
	grey_array[:, :, 1] = grey_intensity
	grey_array[:, :, 2] = grey_intensity
	grey_image_bgr = cv2.cvtColor(grey_array, cv2.COLOR_RGB2BGR)
	cv2.imshow("Image", grey_image_bgr)
	cv2.waitKey(0)  #waits indefinitely until a key is pressed
	cv2.destroyAllWindows()
	return grey_array
