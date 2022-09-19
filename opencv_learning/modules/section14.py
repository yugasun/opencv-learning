import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

file = os.path.join(ASSET_PATH, "13.png")
shape = os.path.join(ASSET_PATH, "shape.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_contour_feature():
    img = cv2.imread(file)

    # convert to gray image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert color to white
    ret, thresh = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    # draw all contours
    cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2)

    # contour area
    area = cv2.contourArea(cnt)
    print(f'Area: {area}')

    # contour perimeter
    perimeter = cv2.arcLength(cnt, True)
    print(f'Perimeter: {perimeter}')

    # image moments
    M = cv2.moments(cnt)
    print(f'M00: {M["m00"]}')
    cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
    print(f'Centroid: {cx}, {cy}')

    # Bounding rectangle
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Min bounding rectangle
    rect = cv2.minAreaRect(cnt)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(img, [box], 0, (255, 0, 0), 2)

    # Min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    (x, y, radius) = np.int0((x, y, radius))
    cv2.circle(img, (x, y), radius, (0, 0, 255), 2)

    # Fit ellipse
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (255, 255, 0), 2)

    # show image
    img_show('img_contour_feature', img)

def img_match_shape():
    img = cv2.imread(shape, 0)

    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh, 3, 2)
    img_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
    print(f'b vs b: {cv2.matchShapes(cnt_b, cnt_b, 1, 0.0)}')
    print(f'b vs c: {cv2.matchShapes(cnt_b, cnt_c, 1, 0.0)}')
    print(f'b vs a: {cv2.matchShapes(cnt_b, cnt_a, 1, 0.0)}')

    img_show('img_match_shape', img_color)
