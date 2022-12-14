import czifile
from skimage import io

img=czifile.imread("test_img1.py")
print(img.shape)