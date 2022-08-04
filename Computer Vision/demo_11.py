import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_hist(img, title, mask=None):
    chans = cv2.split(img)
    colors = ("b","g","r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Nhom")
    plt.ylabel("# of Pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.show()

img = cv2.imread("4.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("img",img)
# plot_hist(img,title="Histogram anh goc")

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask,(120,80),(320,350),255,-1)
cv2.imshow("mask",mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("masked",masked)

plot_hist(img,title="Histogram mask",mask=mask)

cv2.waitKey(0)
cv2.destroyAllWindow()