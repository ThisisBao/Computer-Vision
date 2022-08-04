import cv2
import numpy as np

img = cv2.imread("1.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

s1 = np.ones(img.shape, dtype="uint8")*200
s2 = np.ones(img.shape, dtype="uint8")*100

add = cv2.add(img[20:100,50:200],s1)
sub = cv2.subtract(img,s1)



# print("cv2: max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
# print("cv2: min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
# print("uint8 : {}".format(np.uint8([200]) + np.uint8([100])))
# print("unit8 : {}".format(np.uint8([50]) - np.uint8([100])))

cv2.imshow("img",img)
cv2.imshow("add",add)

cv2.waitKey(0)
cv2.destroyAllWindow()