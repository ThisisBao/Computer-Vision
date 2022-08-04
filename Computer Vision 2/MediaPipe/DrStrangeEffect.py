import HandTrackingModule as htm
import cv2
import cvzone

detector = htm.HandDetector()

cap = cv2.VideoCapture(0)

angle = 0


def calculateDistance(coor1, coor2):
    x1, y1, x2, y2 = coor1[0], coor1[1], coor2[0], coor2[1]
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return dist


while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    imgfront1 = cv2.imread("magic_circle_ccw.png", cv2.IMREAD_UNCHANGED)
    imgfront2 = cv2.imread("magic_circle_cw.png", cv2.IMREAD_UNCHANGED)


    detector.FindHands(img, draw=False)
    lmList = detector.FindPosition(img)
    # Rfingers, Lfingers = detector.FingerUp()
    # totalR = Rfingers.count(1)
    # totalL = Lfingers.count(1)
    # if totalR == 5:
    #     print("Right All Up")
    # if totalL == 5:
    #     print("Left All Up")

    if len(lmList) != 0:
        middle_mcp = lmList[9][1], lmList[9][2]
        wrist = lmList[0][1], lmList[0][2]
        index_tip = lmList[8][1], lmList[8][2]
        pinky_tip = lmList[20][1], lmList[20][2]
        index_mcp = lmList[5][1], lmList[5][2]

        palm = calculateDistance(wrist, index_mcp)
        distance = calculateDistance(index_tip, pinky_tip)

        ratio = distance / palm  # Khoảng cách từ ngón trỏ tới ngón út / Kích thước lòng bàn tay
        if (ratio > 1):  # Khoảng cách từ ngón trỏ tới ngón út > Kích thước lòng bàn tay
            if (ratio > 1.3):
                # get the center of the hand A.K.A the center of the shield
                centerx = middle_mcp[0]  # Điểm trung tâm để đặt ảnh hiệu ứng
                centery = middle_mcp[1]
                print(middle_mcp)
                # determine the diameter of the shield
                shield_size = 3.0
                diameter = round(palm * shield_size)  # Đường kính của ảnh = Kích thước lòng bàn tay x shield_size
                # Mục đích để kích thước hiệu ứng thay đổi phù hợp vs kích thước bàn tay

                # calculate top left corner
                x1 = round(centerx - (diameter / 2))  # điểm trên cùng bên trái
                y1 = round(centery - (diameter / 2))
                h, w, c = img.shape

                # keep the shield inside the frame
                if x1 < 0:
                    x1 = 0
                elif x1 > w:
                    x1 = w

                if y1 < 0:
                    y1 = 0
                elif y1 > h:
                    y1 = h

                if x1 + diameter > w:
                    diameter = w - x1

                if y1 + diameter > h:
                    diameter = h - y1

                shield_size = diameter, diameter
                imgfront1 = cv2.resize(imgfront1, shield_size)
                imgfront2 = cv2.resize(imgfront2, shield_size)
                imgfront1 = cvzone.rotateImage(imgfront1, angle)
                imgfront2 = cvzone.rotateImage(imgfront2, -angle)
                angle += 5

                img = cvzone.overlayPNG(img, imgfront1, [x1,y1])
                img = cvzone.overlayPNG(img, imgfront2, [x1,y1])

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) == ord("q"):
        break
