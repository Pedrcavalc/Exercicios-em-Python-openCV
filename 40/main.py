import cv2

image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('grayscale', grayscale)
cv2.waitKey(0)
# aplicar limiarização
ret, threshhold = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('threshhold', threshhold)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 10))
for i in range(10):
    erosao = cv2.erode(threshhold, kernel, iterations=i)
    cv2.imshow('erosao', erosao)
    cv2.waitKey(1000)
