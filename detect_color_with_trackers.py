## detecting the colors of an image
# import cv2 
# import numpy as np

# frame=cv2.imread("image\download.jpg")

# def nothing(x):
#     pass
# cv2.namedWindow("Color Adjustments")        #creating new windows
# cv2.createTrackbar("lower_h","Color Adjustments",0,225,nothing) #creating trackers
# cv2.createTrackbar("lower_s","Color Adjustments",0,225,nothing)
# cv2.createTrackbar("lower_v","Color Adjustments",0,225,nothing)

# cv2.createTrackbar("upper_h","Color Adjustments",255,225,nothing)
# cv2.createTrackbar("upper_s","Color Adjustments",255,225,nothing)
# cv2.createTrackbar("upper_v","Color Adjustments",255,225,nothing)

# while True:
#     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     l_h=cv2.getTrackbarPos("lower_h","Color Adjustments")       #fetching the tackers
#     l_s=cv2.getTrackbarPos("lower_s","Color Adjustments")
#     l_v=cv2.getTrackbarPos("lower_v","Color Adjustments")

#     u_h=cv2.getTrackbarPos("upper_h","Color Adjustments")
#     u_s=cv2.getTrackbarPos("upper_s","Color Adjustments")
#     u_v=cv2.getTrackbarPos("upper_v","Color Adjustments")

#     lower_bound=np.array([l_h,l_s,l_v]) #giving thw lower value of Hue, saturation, varience
#     upper_bound=np.array([u_h,u_s,u_v])

#     mask=cv2.inRange(hsv,lower_bound,upper_bound)
#     res=cv2.bitwise_and(frame,frame,mask=mask)
#     cv2.imshow("original",frame)
#     cv2.imshow("mask",mask)
#     cv2.imshow("res",res)
#     kwy=cv2.waitKey(1)
#     if kwy==27:
#         break
# cv2.destroyAllWindows()


# detecting color using the webcam
import cv2 
import numpy as np

webcam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
def nothing(x):
    pass
cv2.namedWindow("Color Adjustments")        #creating new windows
cv2.createTrackbar("lower_h","Color Adjustments",0,225,nothing) #creating trackers
cv2.createTrackbar("lower_s","Color Adjustments",0,225,nothing)
cv2.createTrackbar("lower_v","Color Adjustments",0,225,nothing)
cv2.createTrackbar("upper_h","Color Adjustments",255,225,nothing)
cv2.createTrackbar("upper_s","Color Adjustments",255,225,nothing)
cv2.createTrackbar("upper_v","Color Adjustments",255,225,nothing)
while True:
    _,frame=webcam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("lower_h","Color Adjustments")       #fetching the tackers
    l_s=cv2.getTrackbarPos("lower_s","Color Adjustments")
    l_v=cv2.getTrackbarPos("lower_v","Color Adjustments")

    u_h=cv2.getTrackbarPos("upper_h","Color Adjustments")
    u_s=cv2.getTrackbarPos("upper_s","Color Adjustments")
    u_v=cv2.getTrackbarPos("upper_v","Color Adjustments")

    lower_bound=np.array([l_h,l_s,l_v]) #giving thw lower value of Hue, saturation, varience
    upper_bound=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower_bound,upper_bound)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("original",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    kwy=cv2.waitKey(1)
    if kwy==27:
        break
cv2.destroyAllWindows()
