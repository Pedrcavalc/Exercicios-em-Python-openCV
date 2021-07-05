import cv2
import numpy as np
from numba import njit


seed = (0, 0)


@njit
def region_crescimento(image, seed = None):
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


def centroid(image):
    xc, yc = 0, 0
    rows, cols = image.shape[:2]
    count = 0
    for row in range(rows):
        for col in range(cols):
            if image[row, col] == 255:
                xc += row
                yc += col
                count += 1
    xc = int(xc / count)
    yc = int(yc / count)

    return xc, yc


if __name__ == '__main__':
    image = cv2.imread("image.jpg")
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.namedWindow("Clique", 1)
    cv2.imshow("clique", grayscale)
    cv2.setMouseCallback('clique', mouse_event)
    cv2.waitKey(0)

    segmented_image = region_crescimento(grayscale, seed)
    xc, yc = centroid(segmented_image)
    rows, cols = segmented_image.shape[:2]
    nova_img = np.zeros([rows, cols, 3], np.uint8)
    nova_img[np.where(segmented_image == 255)] = [255, 0, 0]
    cv2.circle(nova_img, (yc, xc), 5, (0, 255, 0), -1)
    cv2.imshow('resultado', nova_img)
    cv2.waitKey(0)
