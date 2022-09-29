import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

shapes = os.path.join(ASSET_PATH, "shapes.png")


def join(filename):
    return os.path.join(ASSET_PATH, filename)


def img_show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def img_hough_line():
    img = cv2.imread(shapes)
    drawing = np.zeros(img.shape[:], dtype=np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # get hough lines
    lines = cv2.HoughLines(edges, 0.8, np.pi / 120, 90)
    # if lines is not None:
    #   rho, theta = lines[0][0]
    #   ## Calculate coordinates
    #   u1 = rho / np.cos(theta)
    #   u2 = u1 - height * np.tan(theta)

    # draw lines
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = a * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))

    # draw detect line
    img_show('hough lines', drawing)


def img_hough_line_p():
    img = cv2.imread(shapes)
    drawing = np.zeros(img.shape[:], dtype=np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # get hough lines
    lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90,
                            minLineLength=50, maxLineGap=10)

    # draw lines
    for line in lines:
        x1, y1, x2, y2 = line[0]

        cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255), 1, lineType=cv2.LINE_AA)

    # draw detect line
    img_show('hough lines', drawing)


def img_hough_circle():
    img = cv2.imread(shapes)
    drawing = np.zeros(img.shape[:], dtype=np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=31)
    circles = np.int0(np.around(circles))

    for p in circles[0, :]:
        x, y, r = p
        cv2.circle(drawing, (x, y), r, (0, 255, 0), 2)
        cv2.circle(drawing, (x, y), 2, (0, 0, 255), 3)

    img_show('hough circle', drawing)
