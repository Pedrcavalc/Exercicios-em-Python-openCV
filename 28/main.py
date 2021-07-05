import cv2

image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

imagem_processada = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('resultado',imagem_processada)
cv2.waitKey(0)