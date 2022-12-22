import cv2
img=cv2.imread("image\RGBY.jpg",1)
blue,green,red=cv2.split(img)
img_merged= cv2.merge([blue,green,red])
cv2.imshow("Merged",img_merged)
#blue=img[:,:,0]
cv2.imshow("blue pixel",blue)
cv2.imshow("Green pixel",green)
cv2.imshow("Red pixels",red)
cv2.waitKey(0)
cv2.destroyAllWindos()
#print("Top left",img[0,0] )

#print(img.shape)