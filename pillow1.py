from PIL import Image           #import pillow
import numpy as np              #import numpy
img= Image.open("test_img1.JPG")    #import image
print(type(img))
img.show()
#img.format()
img1=np.asarray(img)
print(type(img1))
from matplotlib import image as mpimg
import matplotlib.pyplot as  plt
img2=mpimg.imread("test_img1.JPG")
# print(type(img2))
# print(img2.shape)
plt.imshow(img2)
plt.colorbar()