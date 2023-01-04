import cv2

video= cv2.VideoCapture("D:\songs\Adhuro - Prabesh Kumar Shrestha [Original] - Copy.mp4")
ret,image=video.read()
count=0
while True:
    if ret==True:
        cv2.imwrite("e:\frame\img%d.jpg"%count,image)
        video.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image=video.read()
        image=cv2.resize(image,(700,450))
        cv2.imshow("res",image)
        count+=1
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
        
video.release()
cv2.destroyAllWindows()