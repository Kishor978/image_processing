from skimage import io 
from matplotlib import pyplot as plt
from skimage import restoration 
img =io.imread("IMG_20221204_131550.jpg",as_gray=True)
import numpy as np
psf=np.ones((3,3))/9
deconvolved, _=restoration.unsupervised_wiener(img,psf)
plt.imsave("d.jpg",deconvolved,cmap='gray')