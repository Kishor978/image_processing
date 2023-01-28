import cv2
import numpy as np
import time
import posemodule as pm
cap = cv2.VideoCapture("E:\image processing\Machine Vision\pose\\v3.mp4")
detector = pm.poseDetector()
dir = 0
count = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (680, 460))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # for left arm
        angle = detector.findAngle(img, 11, 13, 15)
        # for right arm
        # angle=detector.findAngle(img,12,14,16)
        per = np.interp(angle, (200, 240), (0, 100))
        # print(angle,per)
        # check for curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        # print(count)
        cv2.putText(img, str(int(count)), (50, 100),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    kwy = cv2.waitKey(1) & 0xFF
    if kwy == ord('q'):
        break
cv2.destroyAllWindows()
