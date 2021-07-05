import cv2
import numpy as np
import random
image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

canny_image = cv2.Canny(grayscale, 80, 180)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

params.filterByCircularity = False
params.minCircularity = 0.1

params.filterByConvexity = False
params.minConvexity = 0.1

params.filterByInertia = False
params.minInertiaRatio = 0.8

params.minDistBetweenBlobs = 20

detector = cv2.SimpleBlobDetector_create(params)
blobs = detector.detect(canny_image)
print(len(blobs))

rows, cols = image.shape[:2]

for i, k in enumerate(blobs):
    x_up_left = int(k.pt[0] - k.size)
    y_up_left = int(k.pt[1] - k.size)

    x_bot_rigth = int(k.pt[0] + k.size)
    y_bot_rigth = int(k.pt[1] + k.size)

    if x_up_left < 0:
        x_up_left = 0
    if y_up_left < 0:
        y_up_left = 0

    if x_bot_rigth > cols:
        x_bot_rigth = cols
    if y_bot_rigth > rows:
        y_bot_rigth = rows

    crop = image [y_up_left+15:y_bot_rigth-15, x_up_left+15:x_bot_rigth-15]
    cv2.imshow('resultado' + str(i+1), crop)
cv2.imshow('grayscale', grayscale)
cv2.waitKey(0)
