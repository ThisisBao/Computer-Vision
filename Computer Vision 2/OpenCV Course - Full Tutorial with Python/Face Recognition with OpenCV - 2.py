import cv2
import os
import numpy as np

dir = 'test'

people = []
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
for i in os.listdir(dir):
    people.append(i)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

for person in people:
    path = os.path.join(dir,person)
    for img in os.listdir(path):
        img_path = os.path.join(path,img)
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in face:
            face_roi = gray[y:y+h,x:x+w]
            label, confidence = face_recognizer.predict(face_roi)
            print(f'It is {people[label]}!')
            print(label)




