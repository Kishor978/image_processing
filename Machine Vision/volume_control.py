from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import cv2
import time
import numpy as np
import math
import hand_tracking_module as htm

width, height = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
pTime = 0

detector = htm.HandDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4],lmList[8])           #4= thumb tip 8=index fingers tip
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+y1) // 2, (x2+y2)//2  # finding the mid point of line

        cv2.circle(img, (x1, y1), 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x1, y1), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y2)  # measure distance
        # print(length)
        # hand range = 40-300
        # volume range= -65 to 0

        # interperating the range of length into the value of the volume using numpy
        vol = np.interp(length, [40, 300], [minVol, maxVol])
        # in the form of bar range volume0=400 volume100= 150
        volBar = np.interp(length, [40, 300], [400, 150])
        print(int(length), vol)
        # setting the volume as the range
        volume.SetMasterVolumeLevel(vol, None)
        if length < 40:
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    # creating volume bar and setting it unfilled
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    # giving values to the bar
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    # finding FPS and showing it on screen
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    kwy = cv2.waitKey(1) & 0xFF
    if kwy == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
