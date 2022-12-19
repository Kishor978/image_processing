from skimage import io 
from matplotlib import pyplot as plt
img=io.imread("3.jpg",as_gray=True)
from skimage.filters import roberts,sobel,scharr,prewitt
robert=roberts(img)
sobels=sobel(img)
schar=scharr(img)
prewit=prewitt(img)
 
fig, axes=plt.subplots(nrows=2,ncols=3,sharex=True,sharey=True)
ax=axes.ravel()
ax[0].imshow(img,cmap=plt.cm.gray)
ax[0].set_title('original image')

ax[1].imshow(robert,cmap=plt.cm.gray)
ax[1].set_title('roberts')

ax[2].imshow(sobels,cmap=plt.cm.gray)
ax[2].set_title('sobel')

ax[3].imshow(schar,cmap=plt.cm.gray)
ax[3].set_title('scharr')

ax[4].imshow(prewit,cmap=plt.cm.gray)
ax[4].set_title('prewitt')

for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()