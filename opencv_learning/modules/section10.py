import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

avatarFile = os.path.join(ASSET_PATH, "avatar-small.png")
logoFile = os.path.join(ASSET_PATH, "logo.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img, isWait=True):
    cv2.imshow(title, img)
    if isWait:
        cv2.waitKey(0)


# average blur
def img_blur():
    img = cv2.imread(avatarFile)
    blur = cv2.blur(img, (6, 6))

    img_show("blur", blur)


# box filter
def img_filter():
    img = cv2.imread(avatarFile)

    blur = cv2.boxFilter(img, -1, (6, 6), normalize=True)
    img_show("blur", blur)


# gaussian blur
def img_gaussian_blur():
    img = cv2.imread(avatarFile)

    blur = cv2.GaussianBlur(img, (5, 5), 1)
    img_show("blur", blur)


# media blur
def img_median_blur():
    img = cv2.imread(avatarFile)

    blur = cv2.medianBlur(img, 5)
    img_show("blur", blur)


# bilateral blur
def img_bilateral_blur():
    img = cv2.imread(avatarFile)

    blur = cv2.bilateralFilter(img, 9, 75, 75)
    img_show("blur", blur)
