""" 
1. Read image and define pixels(needed to convert the result in micrones not in pixels)
2. Denoising, if required and treshold image to seperate grains from boundry.
3. Clean up image if needed (erode) and create mask for grains
4. lable grains in the masked image
5. measure the properties of each grain (object)
6. output results into a csv file
"""
import cv2 
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io,color, measure
#step 1
img= cv2.imread("image/grains2.jpg",0)
pixels_to_um=0.5                        #1 pixel=0.5 um or 500 nm
#step 2 (denoising is not needed for this image)
#plt.hist(img.flat,bins=100,range=(0,255))
ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#step3
kernal=np.ones((3,3),np.uint8)
eroded=cv2.erode(thresh,kernal,iterations=1)
dilated=cv2.dilate(eroded,kernal,iterations=1)
mask=dilated==255

#step 4
s=[[1,1,1],[1,1,1],[1,1,1]]
labeled_mask,num_lables=ndimage.label(mask,structure=s)
img2=color.label2rgb(labeled_mask,bg_label=0)

#step 5
clusters=measure.regionprops(labeled_mask,img)

#step 6

proplist = ['Area',
            'equivalent_diameter',
            "orientation",
            'MajorAxisLength',
            'MinorAxisLength',
            'Perimeter', 
            'MinIntensity',
            'MeanIntensity',
            'MaxIntensity']
output_file=open("image_measurement.csv",'w')
output_file.write(","+",".join(proplist)+'\n')
for cluster_prop in clusters:
    #output cluster properties to the excel file
    output_file.write(str(cluster_prop['Label']))
    for i,prop in enumerate(proplist):
        if(prop == 'Area'): 
            to_print = cluster_prop[prop]*pixels_to_um**2   #Convert pixel square to um square
        elif(prop == 'orientation'): 
            to_print = cluster_prop[prop]*57.2958  #Convert to degrees from radians
        elif(prop.find('Intensity') < 0):          # Any prop without Intensity in its name
            to_print = cluster_prop[prop]*pixels_to_um
        else: 
            to_print = cluster_prop[prop]     #Reamining props, basically the ones with Intensity in its name
        output_file.write(',' + str(to_print))
    output_file.write('\n')
output_file.close()   #Closes the file, otherwise it would be read only. 




#     print("Label:{} Area:{}".format(prop.label,prop.area))
# io.imshow(mask[250:280,250:280])        #zooming in 
# io.show() 
# cv2.imshow("erode Image",eroded)
# cv2.imshow("dilate Image",dilated)
# cv2.imshow("Thresholded Image",thresh)
# cv2.waitKey(0)