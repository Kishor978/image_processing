import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("image/BSE_Google_Noisy.jpg",0)
# ret,th=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# kernal=m=np.ones((3,3),np.uint8)
# #print(kernal)
# erosion=cv2.erode(th,kernal,iterations=1)
# dilation=cv2.dilate(erosion,kernal,iterations=1)
# #opening=Erosion+dilation
# opening=cv2.morphologyEx(th,cv2.MORPH_OPEN,kernal)
# #plt.hist(img.flat,bins=100,range=(0,255))
# cv2.imshow("Original image",img)
# cv2.imshow("OTSU image",th)
# cv2.imshow("Eroded image",erosion)
# cv2.imshow("Dilated image",dilation)
# cv2.imshow("Opened image",opening)

#alternative
median=cv2.medianBlur(img,3)
ret,th=cv2.threshold(median,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Original image",img)
cv2.imshow("Median image",median)
cv2.imshow("Thresholded image",th)


cv2.waitKey(0)
cv2.destroyAllWindows()