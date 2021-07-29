from pyzbar.pyzbar import decode
import numpy as np
import cv2

#img = cv2.imread('test.jpg')
#code = decode(img)
#print(code)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('main.txt') as f:
    myDatalist = f.read().splitlines()

print(myDatalist)
while True:
    success , img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDatalist:
            myOutput = 'Permitted'
            color = (0,255,0)
        else:
            myOutput = 'Not-Permitted'
            color = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1 , 1 , 2))
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0] , pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        0.9 , color , 2)
        cv2.polylines(img,[pts],True,(255,0,255),5)
    cv2.imshow('Result' , img)
    cv2.waitKey(1)