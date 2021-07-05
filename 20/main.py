import cv2
import numpy as np


from numba import njit


@njit
def region_crescimento( image, seed=None):
    rows, cols = image.shape[:2]
    xc, yc = seed
    segmented = np.zeros_like(image)
    segmented[xc, yc] = 255
    current_found = 0
    previous_point = 1
    while previous_point != current_found:
        previous_point = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                if segmented[row, col] == 255:
                    if image[row-1, col-1] < 127:
                        segmented[row-1, col-1] = 255
                        current_found += 1
                    if image[row-1, col] < 127:
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row-1, col + 1] < 127:
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col-1] < 127:
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col+1] < 127:
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row+1, col-1] < 127:
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row+1, col] < 127:
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row+1, col+1] < 127:
                        segmented[row + 1, col + 1] = 255
                        current_found += 1
        return segmented


if __name__ == '__main__':
    image = cv2.imread("image (1).jpg")
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    segmented_image = region_crescimento(grayscale, seed=(int(grayscale.shape[0]/2), int(grayscale.shape[1]/2)))
