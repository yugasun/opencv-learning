import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

file = os.path.join(ASSET_PATH, "j.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img, isWait=True):
    cv2.imshow(title, img)
    if isWait:
        cv2.waitKey(0)


def img_erode():
    img = cv2.imread(file, 0)

    kernel = np.ones((25, 25), np.uint8)
    erosion = cv2.erode(img, kernel)

    img_show("erode", erosion)


def img_dilate():
    img = cv2.imread(file, 0)

    kernel = np.ones((25, 25), np.uint8)
    dilation = cv2.dilate(img, kernel)

    img_show("dilate", dilation)


def img_morphology():
    file = os.path.join(ASSET_PATH, "school.png")
    img = cv2.imread(file, 0)
    cv2.imshow('source', img)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

    # morph open = src -> erode -> dilate
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening', opening)

    # morph close = src -> dilate -> erode
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing', closing)

    # Gradient = dilation - erosion
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('gradient', gradient)

    # Top hat = src - opening
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow('tophat', tophat)

    # Black hat = closing - src
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow('blackhat', blackhat)

    cv2.waitKey(0)
