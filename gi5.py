import matplotlib.pyplot as plt
import numpy as np

im_1=plt.imread("11.jpg")

print(im_1.shape)

im_2=np.zeros((320,320),dtype=np.uint8)

print(im_2.shape)
im_2=im_1[:,:,0]
#im_3=im_1[:,:,0]
im_3=np.zeros((320,320),dtype=np.uint8)


m,n=im_2.shape
#9karenin ortalamasını alır
for i in  range(1,m-1):
    for j in range(1,n-1):
        s=im_2[i-1,j-1]/9+\
          im_2[i - 1, j]/9+\
          im_2[i-1, j + 1]/9+\
          im_2[i, j -1]/9+\
          im_2[i, j]/9+\
          im_2[i, j+1 ]/9+\
          im_2[i+1,j-1]/9+\
          im_2[i+1,j]/9+\
          im_2[i+1,j+1]/9
        s=int(s)
        im_3[i,j]=s
        #print(s)

plt.subplot(1,2,1)
plt.imshow(im_2,cmap="gray")
plt.subplot(1,2,2)
plt.imshow(im_3,cmap="gray")
plt.show()




