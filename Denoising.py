from skimage import io
from scipy import ndimage as nd
from matplotlib import pyplot as plt
import numpy as np
img=io.imread("noisy_img.jpg")
plt.imshow(img)
plt.show()

gaussian_img=nd.gaussian_filter(img, sigma=3)
plt.imshow(gaussian_img)
plt.show()

median_img=nd.median_filter(img,size=3)
plt.imshow(median_img)
plt.show()

from skimage.restoration import denoise_nl_means,estimate_sigma
sigma_est=np.mean(estimate_sigma(img,multichannel=True))
nlm=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=True,patch_size=5,patch_distance=3,multichannel=True)
plt.imshow(nlm)
plt.show()
