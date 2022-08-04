import cv2
import cvzone
import numpy as np

imgback = cv2.imread("Resources/pc.jpg")

# imgfront = cv2.imread("Resources/gear.png", cv2.IMREAD_UNCHANGED)

# imgfront = cv2.resize(imgfront, (0, 0), None, 0.5, 0.5)

angle = 0

# hf, wf = imgfront.shape[:2]
# hb, wb = imgback.shape[:2]

while True:
    white = np.ones((1080, 720, 3), np.uint8) * 255
    imgfront = cv2.imread("magic_circle_ccw.png", cv2.IMREAD_UNCHANGED)
    imgfront2 = cv2.imread("magic_circle_cw.png", cv2.IMREAD_UNCHANGED)

    imgfront = cvzone.rotateImage(imgfront, angle)
    imgfront2 = cvzone.rotateImage(imgfront2, -angle)

    angle += 5

    result = cvzone.overlayPNG(white, imgfront, [100, 100])
    result = cvzone.overlayPNG(result, imgfront2, [100, 100])
    cv2.imshow("Image", result)

    if cv2.waitKey(1) == ord("q"):
        break
