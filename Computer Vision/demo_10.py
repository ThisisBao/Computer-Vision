import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("4.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("img",img)

img_bray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(img_bray)
cv2.imshow("HE", np.hstack([img_bray,eq]))

cv2.waitKey(0)
cv2.destroyAllWindow()