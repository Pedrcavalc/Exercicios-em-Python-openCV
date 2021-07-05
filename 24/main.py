import cv2
import numpy as np
# definir a seed
seed = (0, 0)


def regiao_crescente(image, seed=None):
    rows, cols = image.shape[:2]

    xc, yc = seed

    cor_ref = image[xc, yc]
    # criar uma matriz
    segmento = np.zeros_like(image)

    segmento[xc, yc] = cor_ref

    atual = 0
    passado = 1

    while passado != atual:
        passado = atual
        atual = 0
        for row in range(rows):
            for col in range(cols):
                if np.array_equal(segmento[row, col], cor_ref):
                    if np.array_equal(segmento[row - 1, col - 1], cor_ref):
                        segmento[row - 1, col - 1] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row - 1, col], cor_ref):
                        segmento[row - 1, col] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row - 1, col + 1], cor_ref):
                        segmento[row - 1, col + 1] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row, col - 1], cor_ref):
                        segmento[row, col - 1] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row, col + 1], cor_ref):
                        segmento[row, col + 1] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row + 1, col - 1], cor_ref):
                        segmento[row + 1, col - 1] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row + 1, col], cor_ref):
                        segmento[row + 1, col] = cor_ref
                        atual += 1
                    if np.array_equal(segmento[row + 1, col + 1], cor_ref):
                        segmento[row + 1, col + 1] = cor_ref
                        atual += 1
        cv2.imshow('Resultadosegmento', segmento)
        cv2.waitKey(1)
    return segmento


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        seed = (y, x)


if __name__ == '__main__':
    image = cv2.imread('image.jpg')
    image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
    cv2.namedWindow('Original', 1)
    cv2.imshow('Original', image)
    cv2.setMouseCallback('Original', mouse_event)
    cv2.waitKey(0)
    segmented_image = regiao_crescente(image, seed)

    cv2.imshow('resultado', segmented_image)
    cv2.waitKey(0)
