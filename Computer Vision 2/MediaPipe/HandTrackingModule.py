import cv2
import mediapipe as mp
import time
from google.protobuf.json_format import MessageToDict

class HandDetector():
    def __init__(self, mode=False, maxHands=2, complexity=1, detection=0.5, tracking=0.5):
        self.static_image_mode = mode
        self.max_num_hands = maxHands
        self.model_complexity = complexity
        self.min_detection_confidence = detection
        self.min_tracking_confidence = tracking

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.model_complexity,
                                        self.min_detection_confidence, self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def FindHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def FindPosition(self, img):
        h, w = img.shape[:2]
        self.lmList = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append([id, cx, cy])
        return self.lmList

    def FingerUp(self):
        rightFingers = []
        leftFingers = []
        tipIds = [4, 8, 12, 16, 20]
        if self.results.multi_hand_landmarks:
            for i in self.results.multi_handedness:
                label = MessageToDict(i)['classification'][0]['label']
                if label == 'Right':
                    if self.lmList[tipIds[0]][1] < self.lmList[tipIds[0] - 2][1]:  # Thumb open
                        rightFingers.append(1)
                    else:  # Thumb close
                        rightFingers.append(0)
                    for id in range(1, 5):
                        if self.lmList[tipIds[id]][2] < self.lmList[tipIds[id] - 2][2]:  # Finger open
                            rightFingers.append(1)
                        else:  # Finger close
                            rightFingers.append(0)

                if label == 'Left':
                    if self.lmList[tipIds[0]][1] > self.lmList[tipIds[0] - 2][1]:  # Thumb open
                        leftFingers.append(1)
                    else:  # Thumb close
                        leftFingers.append(0)
                    for id in range(1, 5):
                        if self.lmList[tipIds[id]][2] < self.lmList[tipIds[id] - 2][2]:  # Finger open
                            leftFingers.append(1)
                        else:  # Finger close
                            leftFingers.append(0)
        return rightFingers, leftFingers

# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(0)
#     detector = HandDetector()
#     while True:
#         _, img = cap.read()
#         img = cv2.flip(img, 1)
#
#         img = detector.FindHands(img)
#         lmList = detector.FindPosition(img)
#
#         if len(lmList) != 0:
#             print(lmList[0])
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
#         cv2.imshow("Camera", img)
#         if cv2.waitKey(1) == ord("q"):
#             break
#
# if __name__ == "__main__":
#     main()