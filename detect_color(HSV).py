#detect color in image
import cv2
import numpy as np

frame=cv2.imread("E:\image processing\image\RGBY.jpg")
while True:
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    upper_val=np.array([110,50,50])
    lower_val=np.array([130,235,225])
    #creating a mask
    mask=cv2.inRange(hsv,lower_val,upper_val)

    #filter mask ith image
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("rea",res)
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()