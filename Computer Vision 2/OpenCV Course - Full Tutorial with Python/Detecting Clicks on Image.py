import cv2
import numpy as np

circles = np.zeros((4, 2), np.int64)  # 4 hàng 2 cột
counter = 0
img = cv2.imread("book.jpg")

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)

while True:
    for x in range(0,4):
        cv2.circle(img, (circles[x][0], circles[x][1]),5,(0,255,255), -1)

    if counter == 4:
        w, h = 250,350
        pts1 = np.float32([circles[0], circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0], [w,0],[w,h],[0,h]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img, matrix, (w,h))
        cv2.imshow("Output", output)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    if cv2.waitKey(1) == ord("q"):
        break
