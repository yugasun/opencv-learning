"""Main module."""

import cv2

ASSET_PATH = "../assets/"
OUTPUT_PATH = "../outputs/"

# copy image to gray
def copy_img():
    img = cv2.imread(ASSET_PATH + "avatar.jpeg", 0)
    cv2.namedWindow("avatar", cv2.WINDOW_NORMAL)
    cv2.imshow("avatar", img)
    cv2.imwrite(OUTPUT_PATH + "avatar_gray.png", img)

copy_img()
