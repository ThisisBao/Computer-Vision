import cv2
import numpy as np


img = cv2.imread("1.jpg")
r = 300/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

(b,g,r) = cv2.split(img) #opencv lưu trữ ảnh RGB như mảng numpy ở trình tự ngược lại: trình tự BGR.

merged = cv2.merge([b,g,r])

z = np.zeros(img.shape[:2], dtype="uint8")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.imshow("HSV", hsv)
cv2.imshow("AnhXam", gray)

# print(b,g,r)
# cv2.imshow("r", r)
# cv2.imshow("g", g)
# cv2.imshow("b", b)
# cv2.imshow("Ghep", merged)
# cv2.imshow("img",img)
# cv2.imshow("R", cv2.merge([z, z, r]))
# cv2.imshow("G", cv2.merge([z, g, z]))
# cv2.imshow("B", cv2.merge([b, z, z]))
cv2.waitKey(0)
cv2.destroyAllWindow()