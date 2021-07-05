import cv2
import numpy as np


image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

canny = cv2.Canny(grayscale, 80, 200)

contornos, heranca = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

imagem_contorno = np.copy(image)

cv2.drawContours(imagem_contorno, contornos, -1, (0, 0, 255), 3)
cv2.imshow('Resultado',imagem_contorno)
cv2.waitKey(0)
