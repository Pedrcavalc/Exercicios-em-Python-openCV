import cv2
import numpy as np

image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('grayscale', grayscale)
ret, threshold_image = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('threshhold', threshold_image)

kernel = np.ones((5,5),np.uint8)
for i in range(7):
    erode = cv2.erode(threshold_image, kernel,iterations=i)
    cv2.imshow('Dilatação' + str([i]), erode)
    cv2.waitKey(1000)