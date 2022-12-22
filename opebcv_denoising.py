import cv2
import numpy as np
import matplotlib.pyplot as plt
#denoising
img =cv2.imread("image/BSE_Google_noisy.jpg",1)
kernel=np.ones((3,3),np.float32)/9
filter_2d=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(3,3))
gauss_blurr=cv2.GaussianBlur(img,(5,5),0)
median_blurr=cv2.medianBlur(img,3)
cv2.imshow("median",median_blurr)               #best
cv2.imshow("Gaussian",gauss_blurr)
bilateral_blur=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral",bilateral_blur)          #best
cv2.imshow("original",img)
cv2.imshow("2D filter ",filter_2d)
cv2.imshow("blur",blur)
#edgedetection
image=cv2.imread("image/786651.jpg")
edges=cv2.Canny(image,100,200)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()