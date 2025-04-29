import numpy as np
import cv2 #OpenCV to manipulate images as arrays

class FileNotFound(Exception):
	pass


def ft_load(path: str) -> np.ndarray:
	try:
		img = cv2.imread(path)
		if img is None:
			raise FileNotFound(f"The specified {path} file was not found or image is empty")
		print(f"The shape of image is: {img.shape}")  # Height, Width, Channels - returns NumPy array - tuple
		img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img_arr = np.array(img_rgb)
		#print(img_arr)
		return (img_arr)
	except FileNotFound as e:
		raise e
	except ValueError as e:
		raise e
	except Exception as e:
		raise Exception(f"Unexpected error: {e}")


# cv2.imshow("Image", img)
# cv2.waitKey(0)  # Wait indefinitely until a key is pressed
# cv2.destroyAllWindows()  # Close the window