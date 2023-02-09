import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import pickle

cap = cv2.VideoCapture("E:\image processing\Machine Vision\game\Video3.mp4")

# veriables and list
frameCounter = 0
countHit = 0
totalScore = 0
hitDrawBallInfoList = []
imgListBallDetected = []

# image wrapping ie.To get image in exact rectangle form
# cornor list contains the location of corner of exact image
cornerPoints = [[377, 52], [944, 71], [261, 624], [1058, 612]]
colorFinder = ColorFinder(False)
hsvVals = {'hmin': 31, 'smin': 32, 'vmin': 0,
           'hmax': 50, 'smax': 255, 'vmax': 255}

# load the polygon file create from sooter_path_picker
with open('E:\image processing\Machine Vision\polygons', 'rb')as f:
    polygonWithScore = pickle.load(f)
# print(polygonWithScore)


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

# function for imageprocessing and return an image


def detectColorDarts(img):
    imgBlur = cv2.GaussianBlur(img, (7, 7), 2)
    imgColor, mask = colorFinder.update(imgBlur, hsvVals)
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.medianBlur(mask, 9)
    mask = cv2.dilate(mask, kernel, iterations=4)
    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # cv2.imshow("Image Color", imgColor)
    return mask


while True:
    frameCounter += 1
    if frameCounter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frameCounter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()

    # img = cv2.imread("E:\image processing\Machine Vision\img.png")

    imgBoard = getBoard(img)
    # getting the preprossed image from function
    mask = detectColorDarts(imgBoard)

# Remove previous detections
    for x, img in enumerate(imgListBallDetected):
        mask = mask-img
        # cv2.imshow(str(x),mask)

    imgContours, conFound = cvzone.findContours(imgBoard, mask, 3500)

    if conFound:
        countHit += 1
        if countHit == 10:
            imgListBallDetected.append(mask)
            # print("Hit Detected")
            countHit = 0
            for polyScore in polygonWithScore:
                center = conFound[0]['center']
                poly = np.array([polyScore[0]], np.int32)
                inside = cv2.pointPolygonTest(poly, center, False)
                # print("inside")
                if inside == 1:
                    hitDrawBallInfoList.append(
                        [conFound[0]['bbox'], conFound[0]['center'], poly])
                    totalScore += polyScore[1]
    print(totalScore)

# creating the blank image for adding images
    imgBlank = np.zeros((imgContours.shape[0],
                         imgContours.shape[1], 3), np.uint8)

# drawing the center point, box and polygon of hit
    for bbox, center, poly in hitDrawBallInfoList:
        cv2.rectangle(imgContours, bbox, (255, 0, 255), 2)
        cv2.circle(imgContours, center, 5, (0, 255, 0), cv2.FILLED)
        cv2.drawContours(imgBlank, poly, -1,
                         color=(0, 255, 0), thickness=cv2.FILLED)

# addind the images
    imgBoard = cv2.addWeighted(imgBoard, 0.7, imgBlank, 0.5, 0)

    # putting the text for total score using cvzone
    imgBoard, _ = cvzone.putTextRect(
        imgBoard, f'Total Score:{totalScore}', (10, 40), scale=2, offset=20)

# stacking the imge countours and image Board which keeps them intacted
    imgStack = cvzone.stackImages([imgContours, imgBoard], 2, 1)

    # cv2.imwrite("E:\image processing\Machine Vision\imgBoard.png", imgBoard)
    # cv2.imshow("Image", img)
    # cv2.imshow("Image Mask", mask)
    # cv2.imshow("ImageBoard", imgBoard)
    cv2.imshow("Image Contour", imgStack)
    kwy = cv2.waitKey(35) & 0xFF
    if kwy == ord('q'):
        break
cv2.destroyAllWindows()
