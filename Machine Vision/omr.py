import cv2
import mediapipe
import numpy as np
import cvzone

path=""
width=680
height=700

img=cv2.imread(path)
cv2.imshow("Image", img)
kwy = cv2.waitKey(1) & 0xFF
if kwy == ord('q'):
    break
cv2.destroyAllWindows()
