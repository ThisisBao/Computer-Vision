import cv2
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
imgback = cv2.imread("Resources/pc.jpg")
white = np.ones((480, 640, 3), np.uint8) * 255
black = np.zeros((480, 640, 3), np.uint8)

imgfront = cv2.imread("magic_circle_ccw.png", cv2.IMREAD_UNCHANGED)
imgfront = cv2.resize(imgfront, (0, 0), None, 0.5, 0.5)

hf, wf = imgfront.shape[:2]
hb, wb = imgback.shape[:2]

fps = cvzone.FPS()

while True:
    _, img = cap.read()
    h, w = img.shape[:2]
    result = cvzone.overlayPNG(img, imgfront, [0, h - hf])

    _, result = fps.update(result)
    cv2.imshow("Image", result)
    if cv2.waitKey(1) == ord("q"):
        break
