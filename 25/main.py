import cv2
import numpy as np
from numba import njit


image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

segmento = np.zeros_like(grayscale)

seed = (0, 0)
event_count = 0


@njit
def regiao_crescente(image, segmento, seed=None):
    rows, cols = image.shape[:2]
    anterior = 1
    atual = 0
    while anterior != atual:
        anterior = atual
        atual = 0
        for row in range(rows):
            for col in range(cols):
                if segmento[row, col] == 1:
                    if image[row-1, col-1] < 230:
                        segmento[row-1, col-1] = 1
                        atual += 1
                    if image[row-1, col] < 230:
                        segmento[row-1, col] = 1
                        atual += 1
                    if image[row-1, col+1] < 230:
                        segmento[row-1, col+1] = 1
                        atual += 1
                    if image[row, col-1] < 230:
                        segmento[row, col-1] = 1
                        atual += 1
                    if image[row, col+1] < 230:
                        segmento[row, col+1] = 1
                        atual += 1
                    if image[row+1, col-1] < 230:
                        segmento[row+1, col+1] = 1
                        atual += 1
                    if image[row+1, col] < 230:
                        segmento[row+1, col] = 1
                        atual += 1
                    if image[row+1, col + 1] < 230:
                        segmento[row+1, col+1] = 1
                        atual += 1
                if segmento[row, col] == 2:
                    if image[row-1, col-1] < 230:
                        segmento[row-1, col-1] = 2
                        atual += 1
                    if image[row-1, col] < 230:
                        segmento[row-1, col] = 2
                        atual += 1
                    if image[row-1, col+1] < 230:
                        segmento[row-1, col+1] = 2
                        atual += 1
                    if image[row, col-1] < 230:
                        segmento[row, col-1] = 2
                        atual += 1
                    if image[row, col+1] < 230:
                        segmento[row, col+1] = 2
                        atual += 1
                    if image[row+1, col-1] < 230:
                        segmento[row+1, col+1] = 2
                        atual += 1
                    if image[row+1, col] < 230:
                        segmento[row+1, col] = 2
                        atual += 1
                    if image[row+1, col + 1] < 230:
                        segmento[row+1, col+1] = 2
                        atual += 1
                if segmento[row, col] == 3:
                    if image[row-1, col-1] < 230:
                        segmento[row-1, col-1] = 3
                        atual += 1
                    if image[row-1, col] < 230:
                        segmento[row-1, col] = 3
                        atual += 1
                    if image[row-1, col+1] < 230:
                        segmento[row-1, col+1] = 3
                        atual += 1
                    if image[row, col-1] < 230:
                        segmento[row, col-1] = 3
                        atual += 1
                    if image[row, col+1] < 230:
                        segmento[row, col+1] = 3
                        atual += 1
                    if image[row+1, col-1] < 230:
                        segmento[row+1, col+1] = 3
                        atual += 1
                    if image[row+1, col] < 230:
                        segmento[row+1, col] = 3
                        atual += 1
                    if image[row+1, col + 1] < 230:
                        segmento[row+1, col+1] = 3
                        atual += 1
    return segmento


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        global event_count
        global segmento
        event_count += 1
        segmento[y, x] = event_count


if __name__ == '__main__':
    cv2.namedWindow('Objeto', 1)
    cv2.imshow('image', grayscale)
    cv2.setMouseCallback('image', mouse_event)
    cv2.waitKey(0)

    imagem_seg = regiao_crescente(grayscale, segmento)

    rows, cols = imagem_seg.shape[:2]
    nova = np.zeros([rows, cols, 3], np.uint8)

    nova[np.where(imagem_seg == 1)] = [0, 0, 255]
    nova[np.where(imagem_seg == 2)] = [255, 0, 0]
    nova[np.where(imagem_seg == 3)] = [0, 255, 0]
    cv2.imshow('Resultado', nova)
    cv2.waitKey(0)