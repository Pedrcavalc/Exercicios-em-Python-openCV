import cv2
image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('grayscale', grayscale)

ret, processamento = cv2.threshold(grayscale,0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('processamento', processamento)

kernel = cv2.getStructuringElement(cv2.MORPH_ERODE, (50, 5))

for i in range(9):
    dilatacao = cv2.dilate(processamento, kernel, iterations=i)
    cv2.imshow('resultado', dilatacao)
    cv2.waitKey(1000)