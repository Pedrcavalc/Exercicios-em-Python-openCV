import cv2
import numpy as np


image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

circle = cv2.HoughCircles(grayscale,cv2.HOUGH_GRADIENT,1,30,param1=150, param2=25,minRadius=0,maxRadius=0)
try:
    circle=np.uint16(np.around(circle))
except AttributeError:
    print("erro, nao ha circulo")
    exit()

img_circle = np.copy(image)

for xc, yc, radius in circle[0, :]:
    cv2.circle(img_circle, (xc, yc), radius, (0, 0, 255), 2)

cv2.imshow('resultado', img_circle)
cv2.waitKey(0)