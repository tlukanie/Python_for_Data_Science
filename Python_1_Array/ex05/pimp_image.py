import numpy as np


def ft_invert(array) -> np.ndarray:
	inverted_array = 255 - array #numpy broadcasting
	return inverted_array

def ft_red(array) -> np.ndarray:
	red_array = array.copy()
	red_array[:, :, 1] = 0
	red_array[:, :, 2] = 0
	return red_array


def ft_green(array) -> np.ndarray:
	green_array = array.copy()
	green_array[:, :, 0] = 0
	green_array[:, :, 2] = 0
	return green_array


def ft_blue(array) -> np.ndarray:
	blue_array = array.copy()
	blue_array[:, :, 0] = 0
	blue_array[:, :, 1] = 1
	return blue_array


def ft_grey(array) -> np.ndarray:
	grey_array = array.copy()
    
    # Initialize the grayscale intensity with the Red channel divided by 3
	grey_intensity = grey_array[:, :, 0] / 3
    
    # Add the Green channel divided by 3
	grey_intensity = grey_intensity + grey_array[:, :, 1] / 3
    
    # Add the Blue channel divided by 3
	grey_intensity = grey_intensity + grey_array[:, :, 2] / 3
    
    # Assign the grayscale intensity to all three channels
	grey_array[:, :, 0] = grey_intensity
	grey_array[:, :, 1] = grey_intensity
	grey_array[:, :, 2] = grey_intensity
	return grey_array

# SHOW IMAGES FROM THE FUNCTIONS