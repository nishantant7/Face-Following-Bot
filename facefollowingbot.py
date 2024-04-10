import cv2
import mediapipe as mp
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy
import serial
import time

arduino = serial.Serial('COM3', 9600)


time.sleep(2)

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        leftPoint = face[374]
        rightPoint = face[145]
        Centre = (320, 240)
        NoseTip = face[1]

        cv2.circle(img, NoseTip, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, Centre, 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, NoseTip, Centre, (0, 0, 255), 3)

        x1, y1 = Centre
        x2, y2 = NoseTip
        xDist = x2-x1

        pt1 = (xDist+320, 240)
        cv2.circle(img, (400, 240), 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (240, 240), 5, (255, 0, 255), cv2.FILLED)

    # Finding focal length
    w, _ = detector.findDistance(leftPoint, rightPoint)
    # f=(w*d)/W
    W = 6.3
    f = 480
    d = int((W*f)/w)

    cvzone.putTextRect(img, f'x2:{int(x2)}',
                       (face[10][0]-100, face[10][1]-50), scale=2)

    command = str(str(x2)+"\n")
    arduino.write(command.encode())
    

    cv2.imshow("image", img)
    cv2.waitKey(1)
