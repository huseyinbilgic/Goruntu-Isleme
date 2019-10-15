
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "mnist-in-csv/"
train_data=np.array(pd.read_csv(data_path + "mnist_train.csv"))
test_data=np.array(pd.read_csv(data_path + "mnist_test.csv"))

print(train_data.ndim,train_data.shape)#785=28*28 +1

print(train_data[10,0])

im_3=train_data[11,:]

print(im_3.shape)

im_4=im_3[1:]

print(im_4.shape)


im_5=im_4.reshape(28,28)
print(im_5)

plt.imshow(im_5,cmap="gray")
plt.show()



m,n=train_data.shape
print(m,n)


import math 

def pdf(x, mu=0.0, sigma=1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma

print(pdf(10,1,3))





#kaç tane k değeri var
def my_counter(k=0):
	s=0
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
	return s


for i in range(10):
	c=my_counter(i)
	print(i,"  ",c)



def get_my_mean_and_std(k=2,l=100):
	#k=0
	s=0
	t=0
	#l=350
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
			
			t+=train_data[i,l+1]
			digit_class=train_data[i,0]
			top_left=train_data[i,1]
			bottom_right=train_data[i,784]
			#print(digit_class,end=" ")
			#print(top_left,end=" ")
			#print(bottom_right,end="\n")
	mean_1=t/s


	s=0
	t=0
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
			diff_1=train_data[i,l+1]-mean_1
			t+=diff_1*diff_1
	std_1=np.sqrt(t/(s-1))
	#var_1=t/(s-1)
	#print(mean_1,std_1)
	return mean_1,std_1
			 

m_1,std_1=get_my_mean_and_std(2,100)
print(pdf(40,m_1,std_1))#40 ın bulunma olasılığı


im_1=plt.imread("yeni1.png")
im_1=im_1[:,:,0]
plt.imshow(im_1,cmap="gray")
plt.show()

print(im_1.shape)
#print(test_values)
#ödev hangi sayı olduğu bul

#plt.imsave("yeni5.jpg",im_1,cmap="gray")

#print(len(train_data))

m,n=im_1.shape
enbuyukpdf=0
enbuyukpdf1=0
sayi=0
for i in range(10):
    enbuyukpdf=0
    for j in range(m):
        for k in range(n):
            test_values=im_1[j,k]
            #print(test_values)
            m_1,std_1=get_my_mean_and_std(i,(28*j)+k)
            #print((28*j)+k)
            if (math.isnan(std_1)==False):
                if(std_1!=0.0):
                    #print("STD\n"+str(std_1))
                    pdf_deger=pdf(test_values,m_1,std_1)
                    if (math.isnan(pdf_deger)==False):
                        if (pdf_deger!=0.0):
                            #print("PDF\n"+str(pdf_deger))
                            #pdf_deger=math.log(pdf_deger)
                            enbuyukpdf+=pdf_deger
                            print(enbuyukpdf)

    if (enbuyukpdf1<enbuyukpdf):
        enbuyukpdf1=enbuyukpdf
        sayi=i
print("Değer")
print(sayi,enbuyukpdf1)




'''



max_1=0
max_digit=0
for i in range(10):
	t=1
	for j in range(784):
		x=im_1[j]
		s=pdf(x,i,j)
		t*=s
		if (t>max_1):
			t=max_1
			max_digit=i
print(max_digit,max_1)
'''

















