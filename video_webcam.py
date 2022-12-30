import cv2

video = cv2.VideoCapture(0)
print( video)
while video.isOpened():
    ret, frame = video.read()
    if ret==True:
        frame=cv2.resize(frame,(700,450))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray frame",gray)
        if cv2.waitKey(1)& 0xFF ==ord('q'): #press to 'q' to exit
            break

video.relese()
cv2.destroyAllWindows()


