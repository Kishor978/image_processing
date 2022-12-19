import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold
import numpy as np
img=io.imread("21Concopy_540x.jpg",as_gray=True)
entropy_img=entropy(img,disk(7 ))
plt.imshow(entropy_img,cmap='gray')
plt.show()
# tyring all the threshold for image
fig,ax=try_all_threshold(entropy_img,figsize=(10,8),verbose=False)
plt.show()

from skimage.filters import threshold_otsu
threshold=threshold_otsu(entropy_img)
binary=entropy_img>=threshold
plt.imshow(binary,cmap='gray')
plt.show()
print("Persent of the bright pixel:",((np.sum(binary==1))*100)/((np.sum(binary==1))+(np.sum(binary==0))))