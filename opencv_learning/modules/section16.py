import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

avatar = os.path.join(ASSET_PATH, "avatar.png")
head = os.path.join(ASSET_PATH, "head.png")
mario = os.path.join(ASSET_PATH, "mario.png")
mario_coin = os.path.join(ASSET_PATH, "mario_coin.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_match():
    img = cv2.imread(avatar, 0)
    template = cv2.imread(head, 0)

    h, w = template.shape[:2]

    # TM_SQDIFF is better than TM_CCOEFF
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # left top point
    left_top = min_loc
    # right bottom point
    right_bottom = (left_top[0] + w, left_top[1] + h)
    # draw match rectangle
    cv2.rectangle(img, left_top, right_bottom, 255, 2)

    img_show('match', img)

def img_multi_match():
    img_rgb = cv2.imread(mario)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(mario_coin, 0)

    h, w = template.shape[:2]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        print(pt)
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)

    img_show('multi_match', img_rgb)
