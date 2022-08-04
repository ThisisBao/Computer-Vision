import cv2
import numpy as np

img = cv2.imread("coin3.png")
r = 500/img.shape[1]
dim = (500, int(r*img.shape[0]))
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("img",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian và Sobel
# lap = cv2.Laplacian(img_gray, cv2.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv2.imshow("Laplacian", lap)
#
# sobelx = cv2.Sobel(img_gray, cv2.CV_64F,1,0)
# sobely = cv2.Sobel(img_gray, cv2.CV_64F,0,1)
#
# sobelx = np.uint8(np.absolute(sobelx))
# sobely = np.uint8(np.absolute(sobely))
# sobelComb = cv2.bitwise_or(sobelx,sobely)
#
# cv2.imshow("Sobel X", sobelx)
# cv2.imshow("Sobel Y", sobelx)
# cv2.imshow("Sobel Combined", sobelComb)

#Phương pháp tách cạnh Canny
# img_gauss = cv2.GaussianBlur(img_gray, (5,5), 0)
#
# canny = cv2.Canny(img_gauss, 30, 150,)
#Tất cả các giá trị gradient lớn hơn ngưỡng 2 được coi là cạnh. Tất cả giá trị nhỏ hơn ngưỡng 1 không được coi là cạnh, và các giá trị nằm giữa được coi là cạnh hoặc không phải cạnh phụ thuộc vào cách các điểm ảnh kết nối theo tần suất lớn hay nhỏ
# cv2.imshow("Canny", canny)





#Đường viền và ứng dụng
img_gauss = cv2.GaussianBlur(img_gray, (25,25), 0)
edged = cv2.Canny(img_gauss, 20, 50)
cv2.imshow("edged",edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("So coin: {}".format(len(cnts)))

coins = img_gray.copy()
cv2.drawContours(coins, cnts, -1, (0,0,0), 2)
cv2.imshow("Coins",coins)

for (i,c) in enumerate(cnts):
    (x,y,w,h) = cv2.boundingRect(c)
    print("Coin {}".format(i+1))
    coin = img_gray[y:y +h, x:x +w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(img_gray.shape[:2], dtype="uint8")
    ((cx,cy), r) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(cx), int(cy)),int(r), 255, -1)
    mask = mask[y:y + h, x:x +w]

    cv2.imshow("Masked Coin", cv2.bitwise_and(coin,coin, mask=mask))


cv2.waitKey(0)
cv2.destroyAllWindows()