import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("image/Alloy.jpg", 0)
equ = cv2.equalizeHist(img)

plt.hist(equ.flat, bins=100, range=(0,100))

cv2.imshow("Original Image", img)
cv2.imshow("Equalized", equ)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit. 
cl1 = clahe.apply(img)

cv2.imshow("CLAHE", cl1)

cv2.waitKey(0)          
cv2.destroyAllWindows()  