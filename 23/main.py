import cv2
import numpy as np
from numba import njit

# definir a seed
seed = (0, 0)


@njit
def regiao_crescente(image, seed=None):
    rows, cols = image.shape[:2]

    xc, yc = seed

    # criar uma matriz
    segmento = np.zeros_like(image)

    segmento[xc, yc] = 255

    atual = 0
    passado = 1

    while passado != atual:
        passado = atual
        atual = 0
        for row in range(rows):
            for col in range(cols):
                if 130 < image[row - 1, col - 1] < 230:
                    segmento[row - 1, col - 1] = 255
                    atual += 1
                if 130 < image[row - 1, col] < 230:
                    segmento[row - 1, col] = 255
                    atual += 1
                if 130 < image[row - 1, col + 1] < 230:
                    segmento[row - 1, col + 1] = 255
                    atual += 1
                if 130 < image[row, col - 1] < 230:
                    segmento[row, col - 1] = 255
                    atual += 1
                if 130 < image[row, col + 1] < 230:
                    segmento[row, col + 1] = 255
                    atual += 1
                if 130 < image[row + 1, col - 1] < 230:
                    segmento[row + 1, col - 1] = 255
                    atual += 1
                if 130 < image[row + 1, col] < 230:
                    segmento[row + 1, col] = 255
                    atual += 1
                if 130 < image[row + 1, col + 1] < 230:
                    segmento[row + 1, col + 1] = 255
                    atual += 1
        return segmento


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        seed = (y, x)


if __name__ == '__main__':
    image = cv2.imread('eren.jpg')
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('clique',1)
    cv2.imshow('original', grayscale)
    cv2.setMouseCallback('Imagem original', mouse_event)
    cv2.waitKey(0)
    segmented_image = regiao_crescente(grayscale, seed)
    cv2.imshow('eren',segmented_image)
    cv2.waitKey(0)
