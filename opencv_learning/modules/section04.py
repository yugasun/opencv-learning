from cmath import log
import os
import cv2

cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

avatar = os.path.join(ASSET_PATH, "avatar.jpeg")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def deal_image():
    img = cv2.imread(avatar)
    px = img[100, 90]
    # [B G R]
    # print(px)
    px_blue = img[100, 90, 0]

    img[100, 90] = [255, 255, 255]

    # B
    # print(px_blue)
    # (行数（高度）, 列数（宽度）, 通道数)
    # print(img.shape)
    height, width, channels = img.shape
    # uint8
    # print(img.size)
    # print(img.dtype)

    # face = img[1000:1400, 800:1100]
    # cv2.imshow("avatar", face)
    # cv2.waitKey(0)
    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))

    b = img[:, :, 0]
    face_blue = b[1000:1400, 800:1100]
    cv2.imshow("blue", face_blue)
    cv2.waitKey(0)
