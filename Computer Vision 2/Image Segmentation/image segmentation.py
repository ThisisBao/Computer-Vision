import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coin.jpeg')
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh3 = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)

print(ret)





plt.figure('Original')
plt.imshow(imgRGB)
plt.figure('Gray')
plt.imshow(imgGray, cmap='gray')
plt.figure('Binary')
plt.imshow(thresh1, cmap='gray')
plt.figure('Otsu')
plt.imshow(thresh2, cmap='gray')
plt.figure('Triangle')
plt.imshow(thresh3, cmap='gray')
plt.show()
