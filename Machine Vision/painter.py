# Steps
# 1. import image
# 2. Find hand land marks
# 3. Check which finger is up
# 4. Is selection mode - Two fingers are up
# 5. If drawing mode - Index finger is ip

import cv2
import time
import numpy as np
import os
import hand_tracking_module as htm

brushThickness = 15
ereaserThickness = 45

# importing the images from folder
folderPath = "E:\image processing\Machine Vision\header"
myList = os.listdir(folderPath)
# print(myList)

overlayList = []
# overlaying the image
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    overlayList.append(image)
# print(len(overlayList))
header = overlayList[0]
drawColor = (255, 0, 255)
# setting the camera screen size
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 168)
detector = htm.HandDetector(detectionCon=0.90)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # importing image
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # finding landmarks
    image = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList)
        
        x1, y1 = lmList[8][1:]  # tip of index finger=8
        x2, y2 = lmList[12][1:]  # tip of middle finger = 12

        fingers = detector.fingersUp()
        # print(fingers)

        # selection mode
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0

            print("Selection mode")
            # checking for clicks
            if y1 < 168:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                if 550 < x1 < 700:
                    header = overlayList[1]
                    drawColor = (255, 255, 0)
                if 750 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                if 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25),
                          (drawColor), cv2.FILLED)

        # drawing mode
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, (drawColor), cv2.FILLED)
            print("Drawing  mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, ereaserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, ereaserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, brushThickness)

            xp, yp = x1, y1
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:168, 0:1280] = header  # setting the header image
    # img=cv2.addWeighted(img,0.5,imgCanvas,0.5,0)   #merging images
    cv2.imshow("image", img)
    cv2.imshow("Canvas", imgCanvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
