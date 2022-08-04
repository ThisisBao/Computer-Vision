import cv2
import pytesseract

def DetectCharacters(img):
    boxes = pytesseract.image_to_boxes(img)
    for box in boxes.splitlines():
        b = box.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


def DetectWords(img):
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x!=0:
            b = b.split()
            if len(b)==12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

def DetectDigits(img):
    config = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_boxes(img, config=config)
    for box in boxes.splitlines():
        b = box.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        print('{} {} {} {}'.format(x,y,w,h))
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('3.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

hImg, wImg, _ = img.shape


#DetectCharacters(img)
#DetectWords(img)
DetectDigits(img)

cv2.imshow('Hi', img)
cv2.waitKey(0)