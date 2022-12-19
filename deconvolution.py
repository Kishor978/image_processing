from skimage import io 
from matplotlib import pyplot as plt
from skimage import restoration 
img =io.imread("de.jpg",as_gray=True)
plt.imshow(img,cmap='gray')
plt.show()
import numpy as np
psf=np.ones((3,3))/9
deconvolved, _=restoration.unsupervised_wiener(img,psf)
plt.imsave("dec.jpg",deconvolved,cmap='gray')