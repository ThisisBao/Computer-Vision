import cv2

img = cv2.imread("endgame.jpg")
r = 600/img.shape[0]
dim = (int(r*img.shape[1]),600)
img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
hImg, wImg = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)