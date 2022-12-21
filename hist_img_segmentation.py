from matplotlib import pyplot as plt
import numpy as np
from skimage import io, img_as_float,img_as_ubyte
from skimage.restoration import denoise_nl_means,estimate_sigma
img=io.imread("BSE_Google_noisy.jpg",as_gray=True)
sigma_est=np.mean(estimate_sigma(img,multichannel=False))
denoise=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=True,patch_size=5,patch_distance=3,multichannel=False)
denoise_ubyte=img_as_ubyte(denoise)
plt.imshow(denoise,cmap='gray')
plt.show()