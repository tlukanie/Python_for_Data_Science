from load_image import ft_load
import numpy as np
import cv2

def rotate_image_left(image):
    height, width = image.shape
    rotated_image = np.zeros((width, height), dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            rotated_image[width - j - 1, i] = image[i, j]
    return rotated_image

def	ft_rotate(path):
    try:
        np_new_obj = ft_load(path)
        # print(f"The shape of image is: {np_new_obj.shape}")
        # print(np_new_obj)
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    try:
        zoomed_obj = np_new_obj[100:500, 450:850]
        bgr_zoomed_obj = cv2.cvtColor(zoomed_obj, cv2.COLOR_RGB2BGR)
        grayscale_obj = cv2.cvtColor(bgr_zoomed_obj, cv2.COLOR_BGR2GRAY) #returns 2d arr
        rotated_obj = rotate_image_left(grayscale_obj)
        grayscale_obj_3d = np.expand_dims(grayscale_obj, axis=-1) #converts into 3darr, adds 1 as a third dimension
        print(f"The shape of image is: {grayscale_obj_3d.shape} or ({grayscale_obj_3d.shape[0]}, {grayscale_obj_3d.shape[1]})")
        print(grayscale_obj_3d)
        print(f"New shape after Transpose: {rotated_obj.shape}")
        print(rotated_obj)
    except Exception as e:
        print(f"Error processing image: {e}")
        return
    
    try:
        # Create a blank canvas larger than the image to include space for axes
        width, height = rotated_obj.shape
        canvas_height = height + 60  #space for the x-axis
        canvas_width = width + 50   #space for the y-axis
        canvas = np.ones((canvas_height, canvas_width), dtype=np.uint8) * 255 #2d arr filled with 1 * 255 (white background)
        
        canvas[10:10 + height, 50:50 + width] = rotated_obj  #placing image at certain row/column
        
        cv2.line(canvas, (50, 10 + height), (50 + width, 10 + height), (0, 0, 0), 2)  #x-axis
        cv2.line(canvas, (49, 10), (49, 10 + height), (0, 0, 0), 2) #y-axis line
        
        for x in range(0, 351, 50):
            cv2.line(canvas, (50 + x, 10 + height), (50 + x, 10 + height + 5), (0, 0, 0), 1) #drawing delimeters
            cv2.putText(canvas, str(x), (50 + x - 10, height + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1) #drawing numbers
        
        for y in range(0, 351, 50):
            cv2.line(canvas, (45, 10 + y), (49, 10 + y), (0, 0, 0), 1)
            cv2.putText(canvas, str(y), (10, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        cv2.imshow("Image", canvas)
        cv2.waitKey(0)  #waits indefinitely until a key is pressed
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error creating canvas or displaying canvas: {e}")
        return

def main():
    try:
        ft_rotate("animal.jpeg")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()