from skimage import io 
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean

img=io.imread("test_img1.jpg")
rescale_img=rescale(img,1.0/4.0,anti_aliasing=True)

resize_img=resize(img,(400,400))

#downscale=downscale_local_mean(img,(4,3))
plt.imshow(resize_img)
plt.show()
plt.imshow(img)
plt.show()