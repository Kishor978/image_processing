import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import pickle


cap = cv2.VideoCapture("E:\image processing\Machine Vision\game\Video2.mp4")
frameCounter = 0
cornerPoints = [[377, 52], [944, 71], [261, 624], [1058, 612]]


def getBoard(img):
    width, height = int(400*1.5), int(380*1.5)
    pts1 = np.float32(cornerPoints)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    for x in range(4):
        cv2.circle(img, (cornerPoints[x][0], cornerPoints[x][1]),
                    15, (0, 255, 0), cv2.FILLED)

    return imgOutput


while True:
    frameCounter += 1
    success, img = cap.read()
    if frameCounter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frameCounter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    imgBoard = getBoard(img)
    cv2.imshow("Image", img)
    cv2.imshow("ImageBoard",imgBoard)
    kwy = cv2.waitKey(35) & 0xFF
    if kwy == ord('q'):
        break
cv2.destroyAllWindows()
