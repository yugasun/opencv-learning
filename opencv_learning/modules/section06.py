import os
import cv2
import matplotlib.pyplot as plt

cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

gradient = os.path.join(ASSET_PATH, "gradient.png")
sudoku = os.path.join(ASSET_PATH, "sudoku.png")

img = cv2.imread(gradient)


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def basic_threshold():

    ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("thresh", th)

    cv2.waitKey(0)


def all_threshold():
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ["Original", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]

    images = [img, th1, th2, th3, th4, th5]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], "gray")
        plt.title(titles[i], fontsize=8)
        plt.xticks([])
        plt.yticks([])
    plt.show()

def auto_threshold():
    img = cv2.imread(sudoku, 0)

    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

    titles = ['Original', 'Global(v = 127)', 'Adaptive Mean', 'Adaptive Gaussian']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], fontsize=8)
        plt.xticks([])
        plt.yticks([])

    plt.show()
