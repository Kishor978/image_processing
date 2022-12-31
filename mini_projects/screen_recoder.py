import cv2
import pyautogui as p
import numpy as np

#create resolution
rs=p.size()
fn=input("Enter file name and path to store: ")
fps=60.0        #frame rate
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(fn,fourcc,fps,rs)

#creating recording module
cv2.namedWindow("Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording",(640,460))
while True:
    img=p.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    # cv2.imshow("recording",f)
    if cv2.waitKey(1)== ord("q"):
        break
output.release()
cv2.destroyAllWindows()