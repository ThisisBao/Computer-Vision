import os

import cv2
import time
import HandTrackingModule as htm

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
# cap.set(3, wCam)
# cap.set(4, hCam)

detector = htm.HandDetector()

pTime = 0
cTime = 0

path = 'images'
list = os.listdir(path)
overlayList = []
for imgPath in list:
    image = cv2.imread(f'{path}/{imgPath}')
    r = 200 / image.shape[0]
    dim = (int(r * image.shape[1]), 200)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    overlayList.append(image)
    # print(image.shape)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    # img = cv2.resize(img, (1280, 720), interpolation=cv2.INTER_AREA)

    img = detector.FindHands(img, draw=True)
    lmList = detector.FindPosition(img)

    if len(lmList) != 0:
        # fingers =[]
        #
        # if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:  # Thumb open
        #     fingers.append(1)
        # else:  # Thumb close
        #     fingers.append(0)
        #
        # for id in range(1,5):
        #     if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]: # Finger open
        #         fingers.append(1)
        #     else: # Finger close
        #         fingers.append(0)
        fingers = detector.FingerUp()
        print(fingers)
        totalFingers = fingers.count(1)

        h, w = overlayList[totalFingers].shape[:2]
        img[0:h, 0:w] = overlayList[totalFingers]

    # print(results.pose_landmarks)
    # if results.pose_landmarks:
    #     poseLms = results.pose_landmarks
    #     for id, lm in enumerate(poseLms.landmark):
    #         cx, cy = int(lm.x*width), int(lm.y*height)
    #         # print(f'{id}: {cx}, {cy}')
    #     mpDraw.draw_landmarks(img, poseLms, mpPose.POSE_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (500,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) == ord("q"):
        break

