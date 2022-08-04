import cv2
import numpy as np

img = np.zeros((600,600,3), dtype="uint8")
# img[20:50,20:50] = (255,255,255)

# cv2.line(img,(0,0),(300,300),color=(134,256,0),thickness=3)
# cv2.line(img,(250,50),(300,80),color=(78,15,100),thickness=3)
#
# cv2.rectangle(img,(200,200),(100,100),color=(150,150,150),thickness=1)
# cv2.rectangle(img,(100,200),(10,90),color=(150,150,150),thickness=-1)

(x,y) = (img.shape[1]//2, img.shape[0]//2)

for r in (0,50):
    cv2.circle(img,(x,y),r,color=(255,200,100),thickness=1)

cv2.imshow("hi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()