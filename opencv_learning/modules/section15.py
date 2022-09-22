import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

file = os.path.join(ASSET_PATH, "hist.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def calc_hist():
    img = cv2.imread(file, 0)

    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # print(hist)
    # img_show('hist', hist)

    # matplotlib draw hist chart
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()

    plt.plot(hist)
    plt.show()

def img_equalize():
    img = cv2.imread(join('mountain.png'), 0)

    # before equalize
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    equ = cv2.equalizeHist(img)

    # cv2.imshow('equalization', np.hstack((img, equ)))
    # cv2.waitKey(0)

    # after equalize
    hist = cv2.calcHist([equ], [0], None, [256], [0, 256])

    # self-adaption equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)

    cv2.imshow('clahe', np.hstack((img, equ, cl1)))
    cv2.waitKey(0)


    # hist = cv2.calcHist([cl1], [0], None, [256], [0, 256])

    # plt.plot(hist)
    # plt.show()
