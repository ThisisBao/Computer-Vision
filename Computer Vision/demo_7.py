import cv2
import numpy as np

img = cv2.imread("5.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

mask = np.zeros(img.shape[:2], dtype="uint8") #shape thì y-hàng đứng trước, x-cột đứng sau
(x,y) = (img.shape[1]//2, img.shape[0]//2)


cv2.rectangle(mask,(350,10),(500,230),255,-1)
cv2.rectangle(mask,(570,10),(730,250),255,-1)





masked = cv2.bitwise_and(img,img,mask=mask)


print(img.shape)
print(x,y)
cv2.imshow("masked",masked)
cv2.imshow("mask",mask)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindow()