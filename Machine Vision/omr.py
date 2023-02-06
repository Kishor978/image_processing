import cv2
import mediapipe
import numpy as np
import cvzone

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()

    cv2.imshow("Image", img)
    kwy = cv2.waitKey(1) & 0xFF
    if kwy == ord('q'):
        break
cv2.destroyAllWindows()
