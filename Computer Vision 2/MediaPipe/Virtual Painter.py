import os
import cv2
import time
import HandTrackingModule as htm
import numpy as np

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)

detector = htm.HandDetector()

pTime = 0
cTime = 0


imgCanvas = np.zeros((480, 640, 3), np.uint8)
while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)

    img = detector.FindHands(img, draw=True)
    lmList = detector.FindPosition(img)

    if len(lmList) != 0:

        x_point, y_point = lmList[8][1:]
        x_middle, y_middle = lmList[12][1:]

        fingers = detector.FingerUp()
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            cv2.rectangle(img, (x_point - 20, y_point - 30), (x_middle + 20, y_middle + 30), (255, 255, 255),
                          cv2.FILLED)
            # print('Erasing mode')
            if xp == 0 and yp == 0:
                xp, yp = x_point, y_point
            # cv2.line(img, (xp, yp), (x_point, y_point), (0, 0, 0), 20)
            cv2.line(imgCanvas, (xp, yp), (x_point, y_point), (0, 0, 0), 20)
            xp, yp = x_point, y_point

        elif fingers[1] and fingers[2] == False:
            cv2.circle(img, (x_point, y_point), 10, (255, 255, 0), cv2.FILLED)
            # print('Drawing mode')
            if xp == 0 and yp == 0:
                xp, yp = x_point, y_point

            cv2.line(img, (xp, yp), (x_point, y_point), (255, 255, 0), 10)
            cv2.line(imgCanvas, (xp, yp), (x_point, y_point), (255, 255, 0), 10)
            xp, yp = x_point, y_point

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (500, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("Hi", img)
    # cv2.imshow("Canvas Image", imgCanvas)
    # cv2.imshow("Inv Canvas Image", imgInv)
    if cv2.waitKey(1) == ord("q"):
        break
