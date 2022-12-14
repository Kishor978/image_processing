from skimage import io, img_as_float,img_as_ubyte
import matplotlib.pyplot as plt

image=io.imread("test_img1.jpg")
image_float=img_as_float(image)
print(image_float)
image_int=img_as_ubyte(image)
print(image_int)
plt.imshow(image)
print(type(image))
plt.show()