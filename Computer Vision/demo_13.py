import cv2
import numpy as np
import mahotas

img = cv2.imread("coin.jpg")
r = 500/img.shape[1]
dim = (500, int(r*img.shape[0]))
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("img",img)

#Phương pháp xét ngưỡng cơ bản
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_gauss = cv2.GaussianBlur(img_gray,(15,15),0)
#
# (T,thresh) = cv2.threshold(img_gauss,155,255, cv2.THRESH_BINARY)
# print(T)
# cv2.imshow("Threshold Binary",thresh)
#
# (T, threshInv) = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY_INV) #ảnh đầu vào là ảnh xám thay thì ảnh có nhiễu Gauss
# cv2.imshow("Threshold Binary Inverse", threshInv)
#
# cv2.imshow("Coins", cv2.bitwise_and(img, img, mask = threshInv))


#Phương pháp ngưỡng thích ứng
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_gauss = cv2.GaussianBlur(img_gray,(15,15),0)
#
# thresh1 = cv2.adaptiveThreshold(img_gauss,255,
#                                cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,4)
# cv2.imshow("Mean Thresh", thresh1)
#
# thresh2 = cv2.adaptiveThreshold(img_gauss, 255,
# 	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
# cv2.imshow("Gaussian Thresh", thresh2)
#
# cv2.imshow("Coins", cv2.bitwise_and(img, img, mask = thresh2))

#Phương pháp Otsu và Riddler-Calvard
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gauss = cv2.GaussianBlur(img_gray,(15,15),0)

T = mahotas.thresholding.otsu(img_gauss)
print("Otsu's threshold: {}".format(T))

thresh = img_gray.copy() #phải là ảnh xám
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.imshow("Coins", cv2.bitwise_and(img, img, mask = thresh))

T = mahotas.thresholding.rc(img_gauss)
print("Riddler-Calvard: {}".format(T))

thresh = img_gray.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)


# cv2.imshow("Gauss",img_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()