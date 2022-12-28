""" 
1.Import 2 images
2.convert to gray
3.Initate ORB detector
4.finf=d key points and describe them
5.MATCH Key points -Brute force matcher
6.RANSAC (reject bad keypoints)
7.Register two images (use homology)

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

im2=cv2.imread("image/monkey.jpg")              #refrence image
im1=cv2.imread("image/monkey_distorted.jpg")  #image to be registered

img1=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(im2 ,cv2.COLOR_BGR2GRAY)

orb=cv2.ORB_create(50)

kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

matcher=cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
# MATCH DESCRIPPTOR
matches=matcher.match(des1,des2,None)
matches=sorted(matches,key=lambda x:x.distance)

points1=np.zeros((len(matches),2),dtype=np.float32)
points2=np.zeros((len(matches),2),dtype=np.float32)

for i,match in enumerate(matches):
    points1[i,:]=kp1[match.queryIdx].pt
    points2[i,:]=kp2[match.trainIdx].pt
    
h, mask=cv2.findHomography(points1,points2,cv2.RANSAC)
# use homography
height, width, channels =im2.shape
im1Reg=cv2.warpPerspective(im1,h,(width,height))

cv2.imshow("Registered image",im1Reg)
cv2.waitKey(0)
    
#img3=cv2.drawMatches(img1,kp1,image1,kp2,matches[:20],None)

#plt.imshow(img3)
#plt.show()

"""img2=cv2.drawKeypoints(img1,kp1,None,flags=None)
image2=cv2.drawKeypoints(image1,kp2,None,flags=None)

plt.imshow(image2)
plt.show()
plt.imshow(img2)
plt.show()"""