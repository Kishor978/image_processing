import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import pickle


cap = cv2.VideoCapture("E:\image processing\Machine Vision\game\Video2.mp4")
frameCounter = 0
cornerPoints = [[377, 52], [944, 71], [261, 624], [1058, 612]]
colorFinder=ColorFinder(False)
hsvVals={'hmin': 31, 'smin': 32, 'vmin': 0, 'hmax': 50, 'smax': 255,'vmax': 255}

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

def detectColorDarts(img):
    imgBlur=cv2.GaussianBlur(img,(7,7),2)
    imgColor,mask=colorFinder.update(imgBlur,hsvVals)
    kernal=np.ones((5,5),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
    cv2.imshow("Image Color",imgColor)
    return mask

while True:
    frameCounter += 1
    if frameCounter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frameCounter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()

    # img = cv2.imread("E:\image processing\Machine Vision\img.png")

    imgBoard = getBoard(img)
    mask=detectColorDarts(imgBoard)
    # cv2.imwrite("E:\image processing\Machine Vision\imgBoard.png", imgBoard)
    cv2.imshow("Image", img)
    cv2.imshow("Image Mask",mask)
    cv2.imshow("ImageBoard", imgBoard)
    kwy = cv2.waitKey(35) & 0xFF 
    if kwy == ord('q'):
        break
cv2.destroyAllWindows()
