from skimage import io, img_as_float
from matplotlib import pyplot as plt
import numpy as np
img=img_as_float(io.imread("Alloy_noisy.jpg"))
#plt.hist(img.flat,bins=100,range=(0,1))

from skimage.restoration import denoise_nl_means,estimate_sigma
sigma_est=np.mean(estimate_sigma(img,multichannel=False))
denoise_img=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=False,patch_size=5,patch_distance=3,multichannel=False)
#plt.imshow(denoise_img,cmap='gray')
#plt.hist(denoise_img.flat,bins=100,range=(0,1))

from skimage import exposure
eq_img=exposure.equalize_adapthist(denoise_img)
#plt.hist(eq_img.flat,bins=100,range=(0,1))

markers=np.zeros(img.shape,dtype=np.uint)
markers[(eq_img<0.6)&(eq_img>0.3)]=1
markers[(eq_img<0.8)&(eq_img>0.99)]=2
#plt.imshow(markers)

from skimage.segmentation import random_walker
labels=random_walker(eq_img,markers,beta=10,mode='bf')
plt.imshow(labels)
# segm1=(labels==1)
# segm2=(labels==2)
# all_segments=np.zeros((eq_img.shape[0]),eq_img.shape[1],1)
# all_segments[segm1]=(1,0,0)
# all_segments[segm2]=(0,1,0)
# plt.imshow(all_segments)