import cv2
import glob
path="image/*"
for file in glob.glob(path):
    print(file)
    a=cv2.imread(file)
    print(a)
    # cv2.imshow("original Image",a)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows
    c=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
    cv2.imshow("Color Image",c)
    cv2.waitKey(0)
    cv2.destroyAllWindows