# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:20:00 2022

@author: thaun
"""
from skimage import io
from matplotlib import pyplot as plt
img=io.imread("test_img1.jpg",as_gray=True)
print(img)
from skimage.filters import roberts,sobel,scharr,prewitt
robort=roberts(img)
plt.imshow(img)