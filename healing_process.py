import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold
img=io.imread("21Concopy_540x.jpg",as_gray=True)
entropy_img=entropy(img,disk(7 ))
plt.imshow(entropy_img,cmap='gray')
plt.show()
#tyring all the threshold for image
#fig,ax=try_all_threshold(entropy_img,figsize=(10,8),verbose=False)
#plt.show()