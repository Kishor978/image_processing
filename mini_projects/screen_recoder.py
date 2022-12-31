import cv2
import pyautogui as p
import numpy as np

#create resolution
rs=p.size()
fn=input("Enter file name and path to store: ")
fps=60.0        #frame rate
fourcc=cv2.VideoWriter_fourcc(*"XVID")  #video ofrmat
output=cv2.VideoWriter(fn,fourcc,fps,rs) #path,codec,frame persec,screenresolution

#creating recording module
cv2.namedWindow("Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording",(640,460))         #resizing frame
while True:
    img=p.screenshot()      #capture frames
    f=np.array(img)         #creating numpy array for captured frame
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)         #writing frame in file
    # cv2.imshow("recording",f)
    if cv2.waitKey(1)== ord("q"):   # press 'q' to quit
        break                       
output.release()
cv2.destroyAllWindows()