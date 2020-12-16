#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

x = input("Enter dimensions. Number only:")
name = input("Enter name of file:")

sz = int(x)

image = np.ones((sz,sz,3))

for i in range(sz):
    if ((i % 2) == 0):
        image[i,:,0] = 0
        image[i,:,2] = 0

#plt.imshow(image)
#plt.show()
plt.imsave(name,image)
