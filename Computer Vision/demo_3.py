import cv2
import numpy as np
img = cv2.imread("4.jpg")
img = cv2.resize(img,(500,600)) #x-w-cột=500, y-h-hàng=600

(h, w) = img.shape[:2]
c = (w // 2, h // 2)

s1 = np.float32([[1,0,25],[0,1,50]])
shift_img = cv2.warpAffine(img, s1, (500,600))
shift_img_2 = cv2.warpAffine(img, s1, (600,500))

s2 = cv2.getRotationMatrix2D(c, 45, 0.5)
rot_img = cv2.warpAffine(img, s2, (w,h))

print(img.shape)
cv2.imshow("hi",img)
# cv2.imshow("shift",shift_img)
# cv2.imshow("shift2",shift_img_2)
cv2.imshow("rotate",rot_img)

cv2.waitKey(0)
cv2.destroyAllWindows()