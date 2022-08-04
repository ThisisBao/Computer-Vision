import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("luffy.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg = img.shape[:2]

blank = np.zeros((hImg, wImg), dtype='uint8')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circle = cv2.circle(blank, (wImg//2, hImg//2), 100, (255,255,255), -1)
mask = cv2.bitwise_and(gray,gray, mask=circle)
cv2.imshow("Mask", mask)

# Grayscale Histogram
gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Numbers of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Color Histogram
mask2 = cv2.bitwise_and(img,img, mask=circle)
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Numbers of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv2.waitKey(0)