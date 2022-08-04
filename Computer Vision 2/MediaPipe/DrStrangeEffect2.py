import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

orange = (0, 140, 255)

coorx = [0] * 21
coory = [0] * 21

wrist = thumb_tip = index_mcp = index_tip = midle_mcp = midle_tip = ring_tip = pinky_tip = (0, 0)

# shield = cv2.imread('magic_circle.png',-1)
shield_1 = cv2.imread('magic_circle_cw.png', -1)
shield_2 = cv2.imread('magic_circle_ccw.png', -1)

deg = 0


def moveData():
    global wrist
    global thumb_tip
    global index_mcp
    global index_tip
    global midle_mcp
    global midle_tip
    global ring_tip
    global pinky_tip
    wrist = coorx[0], coory[0]
    thumb_tip = coorx[4], coory[4]
    index_mcp = coorx[5], coory[5]
    index_tip = coorx[8], coory[8]
    midle_mcp = coorx[9], coory[9]
    midle_tip = coorx[12], coory[12]
    ring_tip = coorx[16], coory[16]
    pinky_tip = coorx[20], coory[20]


def shiningLine(back_img, coor1, coor2, color, size):
    # draw dot
    cv2.circle(img, coor1, size + 1, color, cv2.FILLED)
    cv2.circle(img, coor2, size + 1, color, cv2.FILLED)
    # draw color line
    cv2.line(back_img, coor1, coor2, color, size)
    # draw white line
    cv2.line(back_img, coor1, coor2, (255, 255, 255), round(size / 2))


def drawLine():
    # draw line
    shiningLine(img, thumb_tip, index_tip, orange, 2)
    shiningLine(img, thumb_tip, midle_tip, orange, 2)
    shiningLine(img, thumb_tip, ring_tip, orange, 2)
    shiningLine(img, thumb_tip, pinky_tip, orange, 2)


def drawPentagram():
    # draw pentagram
    shiningLine(img, index_tip, midle_tip, orange, 2)
    shiningLine(img, index_tip, ring_tip, orange, 2)
    shiningLine(img, index_tip, pinky_tip, orange, 2)
    shiningLine(img, midle_tip, ring_tip, orange, 2)
    shiningLine(img, midle_tip, pinky_tip, orange, 2)
    shiningLine(img, ring_tip, pinky_tip, orange, 2)


def calculateDistance(coor1, coor2):
    x1, y1, x2, y2 = coor1[0], coor1[1], coor2[0], coor2[1]
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return dist


def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    bg_img = background_img.copy()  # tạo 1 copy của background_img là ảnh từ camera

    if overlay_size is not None:
        img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)  # overlay_size=shield_size = 3.0

    # Extract the alpha mask of the RGBA image, convert to RGB
    b, g, r, a = cv2.split(img_to_overlay_t)
    # cv2.imshow("a", a)
    overlay_color = cv2.merge((b, g, r))  # ảnh hiệu ứng

    # Apply some simple filtering to remove edge noise
    mask = cv2.medianBlur(a, 5)  # mặt nạ màu đen

    h, w, _ = overlay_color.shape  # kích thước của ảnh hiệu ứng
    roi = bg_img[y:y + h, x:x + w]  # lấy vùng ảnh vừa với ảnh hiệu ứng

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))  # mask chỗ này là ảnh màu trắng
    # cv2.imshow("img1bg", img1_bg)
    # bitwise_and giữ lại phần ảnh chung trên nền trắng
    # bitwise_or giữ lại phần ảnh chung trên nền đen

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

    # Update the original image with our new ROI
    bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return bg_img


while True:
    success, img = cap.read()
    # r = 800 / img.shape[0]
    # dim = (int(r * img.shape[1]), 800)
    # img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                # coorx, coory = int(lm.x * w), int(lm.y * h)
                # cv2.circle(img, (coorx,coory), 6, (0,255,0), cv2.FILLED)
                coorx[id], coory[id] = int(lm.x * w), int(lm.y * h)  # Tọa độ của 21 điểm

            moveData()  # Lưu tọa độ các điểm cần tính
            # drawLine()

            palm = calculateDistance(wrist, index_mcp)
            distance = calculateDistance(index_tip, pinky_tip)
            ratio = distance / palm  # Khoảng cách từ ngón trỏ tới ngón út / Kích thước lòng bàn tay

            if (ratio > 1): # Khoảng cách từ ngón trỏ tới ngón út > Kích thước lòng bàn tay
                # drawPentagram()  # Nếu ratio > 1 thì vẽ hình ngôi sao

                if (ratio > 1.5):
                    # get the center of the hand A.K.A the center of the shield
                    centerx = midle_mcp[0]  # Điểm trung tâm để đặt ảnh hiệu ứng
                    centery = midle_mcp[1]

                    # determine the diameter of the shield
                    shield_size = 3.0
                    diameter = round(palm * shield_size)  # Đường kính của ảnh = Kích thước lòng bàn tay x shield_size
                    # Mục đích để kích thước hiệu ứng thay đổi phù hợp vs kích thước bàn tay

                    # calculate top left corner
                    x1 = round(centerx - (diameter / 2)) # điểm trên cùng bên trái
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
                    # print(shield_size)

                    # increment target angle
                    ang_vel = 2.0
                    deg = deg + ang_vel
                    if deg > 360:
                        deg = 0

                    # get the center of shield
                    hei, wid, col = shield_1.shape
                    cen = (wid // 2, hei // 2)

                    # get rotation matrix
                    M1 = cv2.getRotationMatrix2D(cen, round(deg), 1.0)
                    M2 = cv2.getRotationMatrix2D(cen, round(360 - deg), 1.0)

                    # apply the rotation matrix to image
                    rotated1 = cv2.warpAffine(shield_1, M1, (wid, hei))
                    rotated2 = cv2.warpAffine(shield_2, M2, (wid, hei))

                    # if diameter is exist, add shield
                    if (diameter != 0):
                        img = overlay_transparent(img, rotated1, x1 , y1, shield_size)
                        img = overlay_transparent(img, rotated2, x1, y1, shield_size)

            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord("q"):
        break
