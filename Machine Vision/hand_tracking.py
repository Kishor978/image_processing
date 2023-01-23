import cv2 
import mediapipe as mp
import time
webcam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #capture image from webcam
mpHands= mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success, img=webcam.read() #reading the image 
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # cahanging into rgb
    results=hands.process(imgRGB)   #process the image
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark): # getting informations like coordinates
                #print(id,lm)
                h,w,c=img.shape #getting information  like height,width
                cx,cy= int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id==4: # detecting the specific point 
                    cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)

            mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS) 
            #detect points on hand and connect the points
    cTime=time.time()  #gives current time
    fps=1/(cTime-pTime) #gives fps
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,5),2)
    # dicsplay fps (fimle_name,fps,position,font,scale,color,thickness)
    cv2.imshow("Image",img)
    kwy=cv2.waitKey(1) & 0xFF  
    if kwy ==ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
