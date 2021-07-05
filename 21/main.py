import cv2
import numpy as np
from numba import njit

seed = (0, 0)
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


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        seed = (x, y)


if __name__ == '__main__':
    image = cv2.imread("image (1).jpg")
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.namedWindow("Clique", 1)
    cv2.imshow("clique", grayscale)
    cv2.setMouseCallback('clique', mouse_event)
    cv2.waitKey(0)
    segmented_image = region_crescimento(grayscale, seed)
    cv2.imshow('resultado', segmented_image)
    cv2.waitKey(0)
