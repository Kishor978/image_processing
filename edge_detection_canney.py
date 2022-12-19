from skimage import io
from matplotlib import pyplot as plt
from skimage.feature import canny
img=io.imread("3.jpg",as_gray=True)
edge_canny=canny(img,sigma=4)
plt.imshow(edge_canny)
plt.show()