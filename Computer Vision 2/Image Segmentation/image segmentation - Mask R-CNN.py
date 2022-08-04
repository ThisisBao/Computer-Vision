import cv2
import numpy as np

# Loading Mask RCNN
net = cv2.dnn.readNetFromTensorflow("frozen_inference_graph_coco.pb",
                                    "mask_rcnn_inception_v2_coco_2018_01_28.pbtxt")

colors = np.random.randint(0, 255, (80,3))

img = cv2.imread("res.jpg")
r = 800/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg, _ = img.shape
black = np.zeros((hImg, wImg, 3), np.uint8)
# white = black[:hImg, :wImg]
# white[:] = (255,255,255)



blob = cv2.dnn.blobFromImage(img, swapRB=True)
net.setInput(blob)
boxes, masks = net.forward(["detection_out_final", "detection_masks"])
#print(masks.shape)
#masks = (100, 90, 15, 15)
#boxes = (1, 1, 100, 7)
#print(boxes.shape)


detetions = boxes.shape[2]
for i in range(detetions):
    box = boxes[0,0,i]

    id = box[1]
    score = box[2]
    color = colors[int(id)]
    # print(color)
    if score < 0.5:
        continue

    x1 = int(box[3] * wImg)
    y1 = int(box[4] * hImg)
    x2 = int(box[5] * wImg)
    y2 = int(box[6] * hImg)

    obj = black[y1:y2, x1:x2]
    hObj, wObj, _ = obj.shape
    # print('{} {} {} {}'.format(hObj, wObj, y2-y1, x2-x1))

    mask = masks[i, int(id)]
    mask = cv2.resize(mask, (wObj, hObj))
    ret, mask = cv2.threshold(mask, 0.5, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Mask", mask)
    # cv2.waitKey(0)
    cv2.rectangle(img, (x1,y1), (x2,y2), (int(color[0]), int(color[1]), int(color[2])), 2)

    contours, _ = cv2.findContours(np.array(mask, np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.fillPoly(obj, [contour], (255,255,255))
        # cv2.imshow("object", obj)
        # cv2.waitKey(0)


masked = cv2.bitwise_and(img, black)
blend = cv2.addWeighted(img,0.8,black,0.4,0.8)
print(black.shape)

# cv2.imshow("White", white)
cv2.imshow("Black", black)
cv2.imshow("Image", img)
#cv2.imshow('Image Blending',blend)
cv2.imshow("Masked", masked)
cv2.waitKey(0)