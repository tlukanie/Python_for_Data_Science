from load_image import ft_load
import numpy as np
import cv2

def	ft_zoom(path):
	print(ft_load(path))
	np_new_obj = ft_load(path)
	# print(len(np_new_obj))
	# print(f"coluns: {len(np_new_obj[0])}")
	zoomed_obj = np_new_obj[100:500, 450:850]
	#print(f"New shape after slicing: {zoomed_obj.shape} or ({zoomed_obj.shape[0]}, {zoomed_obj.shape[1]})")
	bgr_zoomed_obj = cv2.cvtColor(zoomed_obj, cv2.COLOR_RGB2BGR)
	grayscale_obj = cv2.cvtColor(bgr_zoomed_obj, cv2.COLOR_BGR2GRAY) #returns 2d arr
	grayscale_obj_3d = np.expand_dims(grayscale_obj, axis=-1) #converts into 3darr, adds 1 as a third dimension
	print(f"New shape after slicing: {grayscale_obj_3d.shape} or ({grayscale_obj_3d.shape[0]}, {grayscale_obj_3d.shape[1]})")
	print(grayscale_obj_3d)
	cv2.imshow("Image", grayscale_obj_3d)
	cv2.waitKey(0)  # Wait indefinitely until a key is pressed
	cv2.destroyAllWindows()  # Close the window

def main():
	ft_zoom("animal.jpeg")


if __name__ == "__main__":
	main()