import cv2
import numpy as np

img = cv2.imread("captain.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Thresholding
ret1, thresh1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
#cv2.imshow("Simple Thresholding", thresh1)

# Adaptive Thresholding
thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
#cv2.imshow("Adaptive Thresholding", thresh2)

# Laplacian Edge Detection
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

# Sobel Edge Detection
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobel = cv2.bitwise_or(sobelx, sobely)
# cv2.imshow("Sobel x", sobelx)
# cv2.imshow("Sobel y", sobely)
# cv2.imshow("Sobel", sobel)

# Canny Edge Detection
canny = cv2.Canny(gray, 150, 175)
#canny = cv2.bitwise_not(canny)
cv2.imshow("Canny", canny)

cv2.imshow("Image", img)
cv2.waitKey(0)