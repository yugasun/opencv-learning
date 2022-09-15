import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

file = os.path.join(ASSET_PATH, "13.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_find_contour():
    img = cv2.imread(file)

    # convert to gray image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert color to white
    ret, thresh = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw all contours
    img_contour = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    # draw first contour in result
    # cnt = contours[0]
    # img_contour = cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)

    # show image
    img_show('img_contour', img_contour)
