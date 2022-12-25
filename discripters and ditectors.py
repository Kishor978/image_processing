
#Harris
import cv2 
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("image/grains.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
Harris=cv2.cornerHarris(gray,2,3,0.04)
img[Harris>0.01*Harris.max()]=[255,0,0]
#cv2.imshow("harris",img)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
########################

import cv2 
import matplotlib.pyplot as plt
import numpy as np
img2=cv2.imread("image/grains.jpg")
gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners=np.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img2,(x,y),3,0,-1)
plt.imshow(img2)
plt.show()
#cv2.imshow("Corners",img2)
cv2.waitKey(0)


#Fast detector#####################
import cv2
image=cv2.imread("image/grains.jpg")
detector=cv2.FastFeatureDetector_create(50)
kp=detector.detect(image,None)
image1=cv2.drawKeypoints(img,kp,None,flags=0)
plt.imshow(image1)
plt.show()

##############BRIEF
#############ORB

import cv2
import numpy as np
from matplotlib import pyplot as plt
image2=cv2.imread("image/download.jpg",0)
orb=cv2.ORB_create(50)
kp,des=orb.detectAndCompute(image2,None)
image3=cv2.drawKeypoints(image2,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(image3)
plt.show()

































