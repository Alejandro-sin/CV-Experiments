import cv2
import numpy as np
from pyzbar.pyzbar import decode

img= cv2.imread('Alejandro_.png')
code = decode(img)



cap = cv2.VideoCapture(0)

# Widh and Higth
cap.set(3, 640)
cap.set(4, 480)


with open('data.txt') as f:
    myList = f.read().splitlines()
    # print(myList)



while True:
    success, img = cap.read()
    for barcode in decode(img):
        # Me devuelve el hiperinculo con los datos.
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        # Chequear si el QR es de la persona o no
        if mydata in myList:
            print("Autorized")
        else:
            print('Un-autorized')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        # Creo el poligono para lectura
        cv2.polylines(img,[pts], True, (255,0,255),5)
        # Creo texto
        pts2 = barcode.rect
        cv2.putText(img, mydata,(pts2[0], pts2[1]),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                    0.9,(255,0,255),2)


    cv2.imshow('Result', img)
    cv2.waitKey(1)


#Escribir autenticación