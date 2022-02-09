import random

n = int(input("Enter no of elements : "))
data = []

for i in range(0,n):
	x = random.random()*100;
	data.append(x)
	

# print(data)

for i in data:
	if i%2!=0:
		print(i,"is odd")