import cv2
import numpy as np

hv = np.zeros((300,300), dtype="uint8")
cv2.rectangle(hv,(25,25),(275,275),255,-1)
ht = np.zeros((300, 300), dtype="uint8")
cv2.circle(ht, (150, 150), 150, 255, -1)

bAND = cv2.bitwise_and(hv,ht)
bOR = cv2.bitwise_or(hv, ht)
bXOR = cv2.bitwise_xor(hv, ht)

cv2.imshow("XOR", bXOR)
cv2.imshow("OR", bOR)
cv2.imshow("AND", bAND)
cv2.imshow("Hinh tron", ht)
cv2.imshow("Hinh vuong",hv)
cv2.waitKey(0)
cv2.destroyAllWindow()