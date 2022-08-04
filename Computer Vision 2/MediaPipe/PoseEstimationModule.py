import cv2
import mediapipe as mp
import time

class PoseDetector():
    def __init__(self, mode=False, complexity=1, smoothLms=True, segmentation=False, smoothSeg=True, detection=0.5, tracking=0.5):
        self.static_image_mode = mode
        self.model_complexity = complexity
        self.smooth_landmarks = smoothLms
        self.enable_segmentation = segmentation
        self.smooth_segmentation = smoothSeg
        self.min_detection_confidence = detection
        self.min_tracking_confidence = tracking

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode, self.model_complexity, self.smooth_landmarks,
                                     self.enable_segmentation, self.smooth_segmentation, self.min_detection_confidence, self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def FindPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def FindPosition(self, img, draw=True):
        lmList = []
        height, width = img.shape[:2]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                cx, cy = int(lm.x * width), int(lm.y * height)
                lmList.append([id,cx,cy])
        return lmList

def main():
    cap = cv2.VideoCapture('ipman.mp4')
    pTime = 0
    cTime = 0
    detector = PoseDetector()
    while True:
        _, img = cap.read()
        r = 600 / img.shape[0]
        dim = (int(r * img.shape[1]), 600)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        img = detector.FindPose(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Video", img)
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()

