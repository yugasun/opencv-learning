import os
import cv2

cwd = os.getcwd()

ASSET_PATH = os.path.join(cwd, "assets/")
OUTPUT_PATH = os.path.join(cwd, "outputs/")

# copy image to gray
def copy_img():
    img = cv2.imread(ASSET_PATH + "avatar.jpeg", 0)
    cv2.namedWindow("avatar", cv2.WINDOW_NORMAL)
    cv2.imshow("avatar", img)
    cv2.imwrite(OUTPUT_PATH + "avatar_gray.png", img)


# open video capture
def open_capture():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    while cv2.waitKey(0) == ord("q"):
        break


# open video capture
def play_video():
    capture = cv2.VideoCapture(ASSET_PATH + "demo.mp4")

    while capture.isOpened():
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("frame", gray)
        if cv2.waitKey(30) == ord("q"):
            break


# record video
def record_video():
    capture = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    outfile = cv2.VideoWriter(OUTPUT_PATH + "record.mp4", fourcc, 30, (640, 480))

    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            outfile.write(frame)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == ord("q"):
                break

        else:
            break
