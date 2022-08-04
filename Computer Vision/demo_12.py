import cv2
import numpy as np

img = cv2.imread("7.jpg")
r = 500/img.shape[1]
dim = (500, int(r*img.shape[0]))
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

#Kĩ thuật tính trung bình
blurred_1 = np.hstack(
    [
        cv2.blur(img,(3,3)),
        cv2.blur(img,(5,5)),
        cv2.blur(img,(7,7))
    ]
)
cv2.imshow("Trung binh",blurred_1)

#Kĩ thuật Gaussian
blurred_2 = np.hstack(
    [
        cv2.GaussianBlur(img,(3,3),0),
        cv2.GaussianBlur(img,(5,5),0),
        cv2.GaussianBlur(img,(7,7),0)
    ]
)

cv2.imshow("Gauss",blurred_2)

#Kĩ thuật trung vị
blurred_3 = np.hstack([
	cv2.medianBlur(img, 3),
	cv2.medianBlur(img, 5),
	cv2.medianBlur(img, 7),
	])

cv2.imshow("Trung vi", blurred_3)

#Kĩ thuật làm mờ song phương
blurred_4 = np.hstack([
	cv2.bilateralFilter(img, 5, 21, 21),
	cv2.bilateralFilter(img, 7, 31, 31),
	cv2.bilateralFilter(img, 9, 41, 41),
	])
cv2.imshow("Bilateral", blurred_4)

#Convert img into sketch
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(img_gray)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(img_gray,invertedblur,scale=256.0)
cv2.imshow("Sketch",sketch)


#cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()