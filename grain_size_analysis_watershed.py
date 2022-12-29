import cv2 
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io,color, measure
img1=cv2.imread("image/grains2.jpg")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
pixels_to_um=0.5
ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)
from skimage.segmentation import clear_border
opening=clear_border(opening)       # clear the boder touchaing grains

sure_bg=cv2.dilate(opening,kernel,iterations=2)
dist_transform=cv2.distanceTransform(opening, cv2.DIST_L2,3)
ret2,sure_fg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
sure_fg=np.uint8(sure_fg) 
unknown=cv2.subtract(sure_bg,sure_fg)
ret3,markers=cv2.connectedComponents(sure_fg)
markers=markers+10
markers[unknown==255]=0
markers=cv2.watershed(img1,markers)
img1[markers==-1]=[0,255,0]
img2=color.label2rgb(markers,bg_label=0)


plt.imshow(markers,cmap="jet")
plt.show()

cv2.imshow("Overlayed orignal image",img1)
cv2.imshow("Colored image",img2)
cv2.waitKey(0)