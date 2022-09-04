import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


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


def draw():
    img = np.zeros((512, 512, 3), np.uint8)

    # draw line
    cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)

    # draw rectangle
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # draw circle
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    # draw ellipse
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (255, 0, 0), -1)

    # draw poly lines
    # define four edge points
    pts = np.array([[10, 5], [50, 10], [70, 20], [20, 30]], np.int32)
    # matrix transfer to 4*1*2
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))

    # use cv2.polylines() to draw multiple lines
    line1 = np.array([[100, 20], [300, 20]], np.int32).reshape((-1, 1, 2))
    line2 = np.array([[100, 60], [300, 60]], np.int32).reshape((-1, 1, 2))
    line3 = np.array([[100, 100], [300, 100]], np.int32).reshape((-1, 1, 2))
    cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))

    # draw text
    # refer to: https://docs.opencv.org/4.6.0/d6/d6e/group__imgproc__draw.html#ga0f9314ea6e35f99bb23f29567fc16e11
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    # refer to: https://docs.opencv.org/3.3.1/d0/de1/group__core.html#gaf076ef45de481ac96e0ab3dc2c29a777
    lineType = cv2.LINE_AA
    cv2.putText(img, "Hello World", (10, 500), font, 2, (255, 255, 255), 2, lineType)

    img_show("img", img)
