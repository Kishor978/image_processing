import cv2
import mediapipe as mp
import time
import math

class poseDetector():
    def __init__(self, mode=False, model_complexity=1,
                 smooth=True,
                 upBody=False,
                 detection_confidence=0.5,
                 tracking_confidence=0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.model_complexity, self.smooth,
                                     self.detection_confidence,
                                     self.tracking_confidence)

    def findPose(self, img, draw=True):

        img = cv2.resize(img, (640, 480))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id,lm)
                cx, cy = int(lm.x*w), int(lm.y*h)

                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 4, (0, 25, 224), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

    # finding angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2)-math.atan2(y1-y2, x1-x2))
        # print(angle)
        if angle < 0:
            angle += 360

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)

            cv2.circle(img, (x1, y1), 7, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 7, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 7, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 0, 255), 2)
        return angle


def main():
    pTime = 0
    cap = cv2.VideoCapture(
        'E:\image processing\Machine Vision\pose\pexels-mikhail-nilov-9362259.mp4')
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)

        # print(lmList)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Image", img)
        kwy = cv2.waitKey(1) & 0xFF
        if kwy == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
