import cv2
import numpy as np

img = cv2.imread("captain.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg = img.shape[:2]

blank = np.zeros((hImg, wImg), dtype='uint8')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 125,175)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv2.drawContours(blank, contours, -1, (255,255,255), 1)

cv2.imshow("Contours Draw", blank)
cv2.imshow("Canny", canny)
cv2.waitKey(0)