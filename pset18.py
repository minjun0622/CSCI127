#Name: Minjun Seo 
#Email: minjun.seo58@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

image = np.ones((30,30,3))

image[:,:10,1] = 0
image[:,:10,2] = 0

image[:,-10:,1] = 0
image[:,-10:,2] = 0

image[-10:,:,1] = 0
image[-10:,:,2] = 0

#plt.imshow(image)
#plt.show()
