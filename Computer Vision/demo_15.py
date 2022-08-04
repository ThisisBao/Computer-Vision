import cv2
import numpy as np
#Bài toán so khớp hình ảnh

img = cv2.imread("house.jpg")
r = 500/img.shape[1]
dim = (500, int(r*img.shape[0]))
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow("img",img)

# (h, w) = img.shape[:2]
# c = (w // 2, h // 2)
# s2 = cv2.getRotationMatrix2D(c, 45, 0.5)
# rot_img = cv2.warpAffine(img, s2, (w,h))
rot_img = cv2.imread("rot_house.png")
r = 500/rot_img.shape[1]
dim = (500, int(r*rot_img.shape[0]))
rot_img = cv2.resize(rot_img,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow("rotate",rot_img)


# orb = cv2.ORB_create(nfeatures=500)
# kp1 = orb.detect(img, None)
# kp2 = orb.detect(rot_img, None)
#
# i1 = cv2.drawKeypoints(img, kp1, None, (0,255,0))
# i2 = cv2.drawKeypoints(rot_img, kp2, None, (0,255,0))


# cv2.imshow("i1", i1)
# cv2.imshow("i2", i2)

# So khớp đặc trưng
orb = cv2.ORB_create(nfeatures=100)
kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(rot_img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

mathch_img = cv2.drawMatches(img, kp1, rot_img, kp2, matches[:10], None)
cv2.imshow("Result", mathch_img)

cv2.waitKey(0)
cv2.destroyAllWindows()