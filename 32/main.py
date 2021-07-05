import cv2
import numpy as np

image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(grayscale, 80, 180)
contornos, quantidade = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(quantidade)

contorno_img = np.copy(image)

cv2.drawContours(contorno_img, contornos, -1, (0, 0, 255), 3)

for i, contorno in enumerate(contornos):
    print('area'+str(i+1) + ':' + str(cv2.contourArea(contorno)))

cv2.imshow('input', grayscale)
cv2.imshow('contorno', contorno_img)
cv2.waitKey(0)