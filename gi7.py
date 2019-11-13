import os
os.getcwd()
os.listdir()

path = os.getcwd() ##'''/usr/share/cups/charmaps'
jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
print(jpg_files)

import numpy as np
import matplotlib.pyplot as plt
im_1=plt.imread(jpg_files[0])
print(type(im_1))

print(im_1.ndim)

print(im_1.shape)

plt.imshow(im_1)
plt.show()


print(im_1.size)

print(im_1[:,:,0]) # 0,1,2 ok, 4 5 error

im_2=im_1[:,:,1]
im_2=im_2-10


def my_rotate_for_RGB(old_image):
    m,n,p=old_image.shape
    new_image=np.zeros((n,m,3),dtype=int) # if dtype=int absent , error
    for i in range(m):
        for j in range(n):
            new_image[j,i,0]=old_image[i,j,0]
            new_image[j,i,1]=old_image[i,j,1]
            new_image[j,i,2]=old_image[i,j,2]
    return new_image


im_4=my_rotate_for_RGB(im_1)
plt.imshow(im_4)
plt.show()




def convert_RGB_to_Gray(old_image_RGB):
    m,n,p=old_image_RGB.shape
    new_image_gray_level=np.zeros((m,n),)
    for i in range(m):
        for j in range(n):
            s=old_image_RGB[i,j,0]+old_image_RGB[i,j,1]+old_image_RGB[i,j,2]
            s=s/3
            new_image_gray_level[i,j]=int(s)
    return new_image_gray_level


def convert_RGB_to_Binary(old_image_RGB,threshold=40):
	m,n,p=old_image_RGB.shape
	new_image_binary=np.zeros((m,n),)
	for i in range(m):
		for j in range(n):
			s=old_image_RGB[i,j,0]+old_image_RGB[i,j,1]+old_image_RGB[i,j,2]
			s=s/3
			if s>threshold:
				new_image_binary[i,j]=1
			else:
				new_image_binary[i,j]=0
	return new_image_binary


im_gray=convert_RGB_to_Gray(im_1)
im_binary=convert_RGB_to_Binary(im_1)

plt.imshow(im_gray,cmap='gray')
plt.show()
plt.imshow(im_binary,cmap='gray')
plt.show()

#print(max(im_1))


im_2=convert_RGB_to_Gray(im_1)
plt.imshow(im_2,cmap='gray')
plt.show()


plt.imsave("new_image.jpg",im_2)
print(im_1.ndim,im_1.shape)


my_histogram_R_G_B={} # R,G,B her biri için ayrı ayrı histogram
m,n,p=im_1.shape
for i in range(m):
	for j in range(n):
		s=(im_1[i,j,0]) # ,im_1[i,j,1],im_1[i,j,2]) # s=im_1[i,j,:], s cannot be Key
		if (2,s) in my_histogram_R_G_B.keys(): # because its type is np.ndar
			my_histogram_R_G_B[(0,s)]=my_histogram_R_G_B[(0,s)]+1
		else:
			my_histogram_R_G_B[(0,s)]=1
my_histogram_R_G_B


# my_histogram_R_G_B={} # R,G,B her biri için ayrı ayrı histogram
m,n,p=im_1.shape
for i in range(m):
	for j in range(n):
		s=(im_1[i,j,1]) # ,im_1[i,j,1],im_1[i,j,2]) # s=im_1[i,j,:], s cannot be Key
		if (1,s) in my_histogram_R_G_B.keys(): # because its type is np.ndar
			my_histogram_R_G_B[(1,s)]=my_histogram_R_G_B[(1,s)]+1
		else:
			my_histogram_R_G_B[(1,s)]=1
my_histogram_R_G_B


t=0
for key in my_histogram_R_G_B.keys():
    t=t+my_histogram_R_G_B[(0,s)]
print(t,m*n)

my_histogram={} # (R,G,B) üçlü histogram


m,n,p=im_1.shape
for i in range(m):
	for j in range(n):
		s=(im_1[i,j,0],im_1[i,j,1],im_1[i,j,2]) # s=im_1[i,j,:], s cannot be Key in di
		if s in my_histogram.keys(): # because its type is np.ndarray
			my_histogram[s]=my_histogram[s]+1
		else:
			my_histogram[s]=1

my_histogram


