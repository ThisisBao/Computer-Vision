import cv2
import numpy as np
img = cv2.imread("2.jpg")

r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# flip_img = cv2.flip(img,-1)
# flip_img2 = cv2.flip(img,0)
# flip_img3 = cv2.flip(img,1)

crop = img[150:400,20:220] # y:150->400 ; x:20->220
img = cv2.rectangle(img,(20,150),(220,400),(255,255,0),2)


print(dim)
print(crop.shape)
cv2.imshow("img",img)
# cv2.imshow("flip",flip_img)
# cv2.imshow("flip2",flip_img2)
# cv2.imshow("flip3",flip_img3)
cv2.imshow("crop",crop)

cv2.waitKey(0)
cv2.destroyAllWindow()