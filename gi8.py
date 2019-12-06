



import random

def my_add(vektor1,vektor2):
	vektor3=[0,0]	
	vektor3[0]=vektor1[0]+vektor2[0]
	vektor3[1]=vektor1[1]+vektor2[1]
	return vektor3

def my_center(vektor_1,vektor_2):
	s=len(vektor_1)
	result_vek=[]
	for i in range(s):
		temp=(vektor_1[i]+vektor_2[i])/2
		result_vek.append(temp)
	return result_vek





#m,n=10,3
def my_create_vectors(m=5,n=2):
	my_vec=[]
	for i in range(m):
		my_vec.append([])
		for j in range(n):
			my_vec[i].append(random.randint(-10,10))
	return my_vec

v_1=[1,3,1]
v_2=[-2,-3,6]
print(my_create_vectors())
#print(my_add(v_1,v_2))
print(my_center(v_1,v_2))


def my_instance(v_1,v_2):
	s=len(v_1)
	t=0
	for i in range(s):
		t+=(v_1[i]-v_2[i])**2
	return t**0.5


vector_1=[0,4,0]
vector_2=[3,0,0]

print(my_instance(vector_1,vector_2))







