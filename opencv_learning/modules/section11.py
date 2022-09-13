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


def img_show(title, img, isWait=True):
    cv2.imshow(title, img)
    if isWait:
        cv2.waitKey(0)


# average blur
def img_canny_detect():
    img = cv2.imread(file, 0)

    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    edges = cv2.Canny(thresh, 30, 70)
    edge_img = np.hstack((img, thresh, edges))

    img_show("canny", edge_img)

