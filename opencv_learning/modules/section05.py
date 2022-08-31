import os
import cv2
import numpy as np

cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

avatar = os.path.join(ASSET_PATH, "avatar.jpeg")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def convert_image():
    img = cv2.imread(avatar)

    # convert to gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("img", img)
    # cv2.imshow("gray", img_gray)
    # cv2.waitKey(0)

    # print flags
    flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
    print(flags)


def capture_blue():
    capture = cv2.VideoCapture(0)

    # Adjust it on lightness
    # lower blue color
    lower_blue = np.array([100, 110, 110])
    # upper blue color
    upper_blue = np.array([130, 255, 255])

    while True:
        # 1. Capture one frame from video
        ret, frame = capture.read()

        # 2. Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 3. inRange() between lower to upper color
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 4. Only keep blue color
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

        if cv2.waitKey(1) == ord("q"):
            break
