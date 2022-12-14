import cv2
from matplotlib import pyplot as plt
img=cv2.imread("test_img1.jpg",0)
# plt.imshow(img)
# plt.show()
cv2.imshow("Gray Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()