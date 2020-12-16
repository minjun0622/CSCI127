#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0

plt.imsave('reds.png', img2)  #Save the image we created to the file: reds.png
