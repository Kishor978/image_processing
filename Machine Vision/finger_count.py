import cv2
import time
import os
import hand_tracking_module as htm

width, height = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

path = "E:\image processing\Machine Vision\Fingers"
mylist = os.listdir(path)  # getting list of images
print(mylist)

overlayList = []
for imPath in mylist:
    image = cv2.imread(f'{path}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
pTime = 0

detector = htm.HandDetector(detectionCon=0.75)

tipsId = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []
        # for thumb
        if lmList[tipsId[0]][2] < lmList[tipsId[0]-1][2]:
            fingers.append(1)
        else:
            fingers.append(0)
        # for other fingers
        for id in range(1, 5):
            if lmList[tipsId[id]][2] < lmList[tipsId[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
            # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        # overlaying image
        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (400, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    kwy = cv2.waitKey(1) & 0xFF
    if kwy == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
