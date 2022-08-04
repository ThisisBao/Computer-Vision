import cv2
import numpy as np

img = cv2.imread("zoro.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg = img.shape[:2]

# Blur
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
average_blur = cv2.blur(img, (3,3))
cv2.imshow("Average Blur", average_blur)
median_blur = cv2.medianBlur(img, 3)
cv2.imshow("Median Blur", median_blur)
bilateral_blur = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow("Bilateral", bilateral_blur)


# Edge Cascade
canny = cv2.Canny(blur, 125, 175)
draw = 255-canny

# Dilate
dilate = cv2.dilate(canny, (5,5), iterations=3)

# Erode
erode = cv2.erode(dilate, (5,5), iterations=4)

# Translation -x:Left    +x:Right     -y:Up    +y:Down
def translate(img, x ,y):
    matrix = np.float32([[1,0,x], [0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, matrix, dim)

translated = translate(img, 100, 100)

# Rotation
def rotate(img, angle, rotatePoint=None):
    if rotatePoint is None:
        rotatePoint = (wImg//2, hImg//2)
    matrix = cv2.getRotationMatrix2D(rotatePoint, angle, 1)
    dim = (wImg, hImg)
    return cv2.warpAffine(img, matrix, dim)

rotated = rotate(img, -45)

# Flip
flip = cv2.flip(img, -1)

# cv2.imshow("Translated", translated)
# cv2.imshow("Rotated", rotated)
#cv2.imshow("Flip", flip)
# cv2.imshow("Canny", canny)
#cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
# cv2.imshow("Dilate", dilate)
# cv2.imshow("Draw", draw)
# cv2.imshow("Erode", erode)
cv2.waitKey(0)