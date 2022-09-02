import os
import cv2
import numpy as np

cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

avatar = os.path.join(ASSET_PATH, "avatar.png")

img = cv2.imread(avatar)


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_resize():
    # shrink image size to 400x400
    res = cv2.resize(img, (400, 400))

    # zoom image to 2 times
    res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    cv2.imshow("shrink", res)
    cv2.imshow("zoom", res2)

    cv2.waitKey(0)


def img_flip():
    # the second argument can be:
    # 1 - horizontal flip
    # 0 - vertical flip
    # -1 - horizontal and vertical flip
    res = cv2.flip(img, 0)

    cv2.imshow("flip", res)
    img_show("flip", res)


def img_move():
    rows, cols = img.shape[:2]

    # define move matrix
    M = np.float32([[1, 0, 200], [0, 1, 100]])

    # use affine warp to move image
    dst = cv2.warpAffine(img, M, (cols, rows))

    img_show("shift", dst)


def img_rotate():
    rows, cols = img.shape[:2]

    # rotate 45deg and zoom out to 2 times
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)

    dst = cv2.warpAffine(img, M, (cols, rows))

    img_show("rotation", dst)
