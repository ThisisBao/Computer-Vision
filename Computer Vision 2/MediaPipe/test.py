import cv2

img = cv2.imread("magic_circle_cw.png")

b, g, r = cv2.split(img)
b = (1, 1, 1)
r = (1, 1, 1)

img = cv2.merge((b, g, r))

cv2.imshow("hi", img)
cv2.waitKey(0)
