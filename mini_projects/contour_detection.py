#contour detection using color space
import cv2
import numpy as np
#read camera
webcam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass
# creating window
cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Color Adjustments",(300,300))
cv2.createTrackbar("Thresh","Color Adjustments",0,225,nothing) #creating trackers

#color detection track
cv2.createTrackbar("lower_h","Color Adjustments",0,225,nothing) #creating trackers
cv2.createTrackbar("lower_s","Color Adjustments",0,225,nothing)
cv2.createTrackbar("lower_v","Color Adjustments",0,225,nothing)
cv2.createTrackbar("upper_h","Color Adjustments",255,225,nothing)
cv2.createTrackbar("upper_s","Color Adjustments",255,225,nothing)
cv2.createTrackbar("upper_v","Color Adjustments",255,225,nothing)
while True:
    _,frame=webcam.read()
    frame=cv2.resize(frame,(300,300))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("lower_h","Color Adjustments")       #fetching the tackers
    l_s=cv2.getTrackbarPos("lower_s","Color Adjustments")
    l_v=cv2.getTrackbarPos("lower_v","Color Adjustments")

    u_h=cv2.getTrackbarPos("upper_h","Color Adjustments")
    u_s=cv2.getTrackbarPos("upper_s","Color Adjustments")
    u_v=cv2.getTrackbarPos("upper_v","Color Adjustments")

    lower_bound=np.array([l_h,l_s,l_v]) #giving thw lower value of Hue, saturation, varience
    upper_bound=np.array([u_h,u_s,u_v])
#creating mask
    mask=cv2.inRange(hsv,lower_bound,upper_bound)
    #filter mask with image
    filtr=cv2.bitwise_and(frame,frame,mask=mask) #back ground white balck

#reverse mask (background white)
    maskr=cv2.bitwise_not(mask)
    t_g=cv2.getTrackbarPos("Thresh","Color Adjustments")
    ret,thresh=cv2.threshold(maskr,t_g,255,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thresh,(1,1),iterations=6)

    cnts,hier=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cnts =list of contours which is an array with x,y coordinates
    #hier= hierarchy variable and contains inamge informatiom
   # frame=cv2.drawContours(frame,cnts,-1,(176,10,15),4)
    for c in cnts:
        epsilon=0.0001*cv2.arcLength(c,True)
        data=cv2.approxPolyDP(c,epsilon,True)
        hull=cv2.convexHull(data)
        cv2.drawContours(frame,[c],-1,(50,50,150),2)
        cv2.drawContours(frame,[hull],-1,(0,255,0),2)
    cv2.imshow("thresh",thresh)
    cv2.imshow("mask",mask)
    cv2.imshow("filterr",filtr)
    cv2.imshow("rasult",frame)
    kwy=cv2.waitKey(1) & 0xFF
    if kwy==27:
        break
webcam.release()
cv2.destroyAllWindows()
