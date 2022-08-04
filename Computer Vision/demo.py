import cv2
import argparse


img = cv2.imread("3.jpg")

(b,g,r) = img[0,0]
print("Giá trị ở tọa độ (0,0) - R: {}, G: {}, B: {}".format(r,g,b))

c1 = img[0:200,0:400]
cv2.imshow("test", c1)

img[0:200,0:400] = (195,187,197)


# new_img = cv2.resize(img,(600,400))
# gray_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# binary = cv2.threshold(gray_bgr, thresh=127,maxval=255, type=cv2.THRESH_BINARY)[1]
# rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# gray_rgb = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

# print(img.shape)
cv2.imshow("img",img)
# cv2.imshow("gray_bgr",gray_bgr)
# cv2.imshow("binary",binary)
# cv2.imshow("rgb",rgb)
# cv2.imshow("gray_rgb",gray_rgb)

cv2.waitKey(0)
cv2.destroyAllWindow()