import cv2
video = cv2.VideoCapture("new/MERO_YO_MAAN_LE_AaJA.mp4")
print("video", video)
while True:
    ret, frame = video.read()
    frame=cv2.resize(frame,(700,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.imshow("gray frame",gray)
    k=cv2.waitKey(25)& 0xFF         #mask=0xFF
    if k==ord("q"):
        break
video.release()
cv2.destroyAllWindows()


