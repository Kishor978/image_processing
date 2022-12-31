"""Steps to access the camera using mobile.
1.download "IP webcam"App from play store
2. open it and run the server
3. put ip address the laptops browser (Make sure both device are connected with same wifi network)
4. camera is accessed through mobile """

import cv2
camera="http://192.168.1.13:8080/video"
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
video.open(camera)
print("check===",video.isOpened())
fourcc=cv2.VideoWriter_fourcc(*"xvid")
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) 
print( video)
while video.isOpened():
    ret, frame = video.read()
    if ret==True:
        frame=cv2.resize(frame,(640,480))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray frame",gray)
        output.write(frame)
        if cv2.waitKey(1)& 0xFF ==ord('q'): #press to 'q' to exit
            break

video.release()
output.release()
cv2.destroyAllWindows()

