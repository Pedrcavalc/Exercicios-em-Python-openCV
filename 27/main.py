import cv2
import numpy as np
import random
from numba import njit


@njit


def crescimento_regiao(image):
    rows, cols = image.shape[:2]
    segmento = np.zeros_like(image)
    n_objetos = 0
    for aux_row in range(rows):
        for aux_col in range(cols):
            if segmento[aux_row, aux_col] == 0 and image[aux_row, aux_col] < 230:
                n_objetos += 1
                segmento[aux_row, aux_col] = n_objetos
                atual = 0
                antigo = 1
                while atual != antigo:
                    antigo = atual
                    atual = 0

                    for row in range(rows):
                        for col in range(cols):
                            if segmento[row, col] == n_objetos:
                                if image[row-1, col-1] < 230:
                                    segmento[row-1, col-1] = n_objetos
                                    atual += 1
                                if image[row-1, col] < 230:
                                    segmento[row-1, col] = n_objetos
                                    atual += 1
                                if image[row - 1, col + 1] < 230:
                                    segmento[row - 1, col + 1] = n_objetos
                                    atual += 1
                                if image[row, col-1] < 230:
                                    segmento[row, col-1] = n_objetos
                                    atual += 1
                                if image[row, col+1] < 230:
                                    segmento[row, col+1] = n_objetos
                                    atual += 1
                                if image[row+1, col-1] < 230:
                                    segmento[row+1, col-1] = n_objetos
                                    atual += 1
                                if image[row+1, col] < 230:
                                    segmento[row+1, col] = n_objetos
                                    atual += 1
                                if image[row+1, col+1] < 230:
                                    segmento[row+1, col+1] = n_objetos
                                    atual += 1
    return segmento, n_objetos


if __name__ == '__main__':
    image = cv2.imread('image (1).jpg')

    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    cv2.imshow('original', grayscale)

    segmento, n_objetos = crescimento_regiao(grayscale)

    rows, cols = segmento.shape[:2]
    nova_imagem = np.zeros([rows, cols, 3], np.uint8)

    for n in range(n_objetos):
        color = lambda: random.randint(0, 255)

        x_min = 0
        x_max = 0
        y_min = 0
        y_max = 0
        for row in range(rows):
            for col in range(cols):
                if segmento [row,col] == n+1:
                    if x_max < col:
                        x_max=col
                    if x_min > col:
                        x_min = col
                    if y_max < row:
                        y_max = row
                    if y_min > row:
                        y_min = row
                    if x_min == 0:
                        x_min = x_max
                    if y_min == 0:
                        y_min = y_max
        nova_imagem[np.where(segmento == n + 1)] = [color(), color(), color()]
        resultado = nova_imagem[y_min:y_max, x_min:x_max]

        cv2.imshow('objeto'+ str(n),resultado)
        cv2.waitKey(5)
    cv2.waitKey(0)


