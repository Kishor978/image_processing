import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self,mode=False,
                 upBody=False,
                 smooth=True,
                 detection_confidence=0.5,
                 tracking_confidence=0.5):
        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detection_confidence=detection_confidence
        self.tracking_confidence=tracking_confidence

        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(self.mode,self.upBody,self.smooth,
                                   self.detection_confidence,
                                   self.tracking_confidence)
    def findPose(self,img,draw=True):

        img=cv2.resize(img,(640,480))
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=self.pose.process(imgRGB)

        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,results.pose_landmarks,
                                               self.mpPose.POSE_CONNECTIONS)
        return img
        # for id,lm in enumerate(results.pose_landmarks.landmark):
        #     h,w,c=img.shape
        #     cx,cy=int(lm.x*w),int(lm.y*h)
        #     cv2.circle(img,(cx,cy),4,(0,25,224),cv2.FILLED)


def main():
    pTime = 0
    cap = cv2.VideoCapture('E:\image processing\Machine Vision\pose\pexels-mikhail-nilov-9362259.mp4')
    detector =poseDetector()
    while True: 
        success, img = cap.read()
        img=detector.findPose(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__=="__main__":
    main()
