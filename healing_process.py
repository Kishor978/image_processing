import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu
import glob
time=0
time_list=[]
area_list=[]
path="Scratch_assay/*"
for file in glob.glob(path):
    img=io.imread(file)
    entropy_img=entropy(img,disk(7 ))
    threshold=threshold_otsu(entropy_img)
    binary=entropy_img<=threshold
    scratch_area=np.sum(binary==True)
    print(time , scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time+=1 
plt.plot(time_list,area_list)
from scipy.stats import linregress
#print(linregress(time_list,area_list))
slop,itercept,r_value,p_value,std_err=linregress(time_list,area_list)
