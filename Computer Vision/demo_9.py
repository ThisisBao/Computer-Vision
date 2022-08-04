import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("4.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("img",img)

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",img_gray)
# H = cv2.calcHist([img_gray],channels=[0],mask=None,histSize=[256],ranges=[0,256])

# plt.figure()
# plt.title("Histogram anh xam")
# plt.xlabel("Nhom")
# plt.ylabel("# of Pixels")
# plt.plot(H)
# plt.xlim([0,256])
# plt.show()

chans = cv2.split(img)
colors = ("b","g","r")
plt.figure()
plt.title("Histogram anh mau")
plt.xlabel("Nhom")
plt.ylabel("# of Pixels")

for (chan,color) in zip(chans,colors):
    H = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(H,color = color)
    plt.xlim([0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindow()