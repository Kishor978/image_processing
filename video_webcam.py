# import cv2

# video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# print( video)
# while video.isOpened():
#     ret, frame = video.read()
#     if ret==True:
#         frame=cv2.resize(frame,(700,450))
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow("frame", frame)
#         cv2.imshow("gray frame",gray)
#         if cv2.waitKey(1)& 0xFF ==ord('q'): #press to 'q' to exit
#             break

# video.release()
# cv2.destroyAllWindows()


#saving the video
import cv2

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# video foramts DIVX,XVID.X264,WMI1,WMI2
#XVID IS RECOMENDED
fourcc=cv2.VideoWriter_fourcc(*"xvid")
#4 parameters name, codec,fps,resolution 
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #o for gray as extra perimeter
print( video)
while video.isOpened():
    ret, frame = video.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray frame",gray)
        output.write(frame)
        if cv2.waitKey(1)& 0xFF ==ord('q'): #press to 'q' to exit
            break

video.release()
output.release()
cv2.destroyAllWindows()

