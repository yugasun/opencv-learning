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


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_merge():
    img1 = cv2.imread(avatarFile)
    img2 = cv2.imread(logoFile)

    res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

    img_show("merge", res)


def img_mix():
    img1 = cv2.imread(avatarFile)
    img2 = cv2.imread(logoFile)

    # place logo to left-top
    rows, cols = img2.shape[:2]
    roi = img1[:rows, :cols]

    # create mask
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # img_show("mix", mask_inv)

    # keep background except logo
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    # merge image
    dst = cv2.add(img1_bg, img2)
    # place in source image
    img1[:rows, :cols] = dst

    img_show("mix", img1)
