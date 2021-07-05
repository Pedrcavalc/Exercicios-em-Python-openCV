import cv2
import numpy as np


image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('grayscale',grayscale)
cv2.waitKey(0)
canny = cv2.Canny(grayscale, 80, 200)

contornos, heranca = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
del canny, heranca
poligono = [None] * len(contornos)
retangulo = [None] * len(contornos)

for i, contorno in enumerate(contornos):
    poligono[i] = cv2.approxPolyDP(contorno, 2, True)
    retangulo[i] = cv2.boundingRect(poligono[i])
print(len(retangulo))
imagem_contornada = np.copy(image)
del image

for i, contorno in enumerate(poligono):
    cv2.rectangle(imagem_contornada, (int(retangulo[i][0]), int(retangulo[i][1])),
                  (int(retangulo[i][0]) + int(retangulo[i][2]), int(retangulo[i][1]) + retangulo[i][3]),
                  (255, 0, 0), 2)

    separacao = imagem_contornada[int(retangulo[i][1]):int(retangulo[i][1])+retangulo[i][3], int(retangulo[i][0]):
                                  int(retangulo[i][0])+int(retangulo[i][2])]
    print('rodou')
    cv2.imshow('objeto' + str(i+1), separacao)
    cv2.waitKey(10)
    del separacao

cv2.imshow('Entrada', grayscale)
del grayscale
cv2.imshow('resultado', imagem_contornada)
cv2.waitKey(0)
