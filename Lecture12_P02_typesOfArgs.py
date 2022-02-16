
def sum1(a,b):
	print("a : ",a,"\t b : ",b," result : ",a+b)

sum1(3,4)# normal


def sum2(a,b=10):  #default args  
	print("a : ",a,"\t b : ",b," result : ",a+b,"\n")

sum2(1,2)# normal
x = 3
sum2(x) # default args 
sum2() #??


def sum3(a,b): #keyword?
	print("a : ",a,"\t b : ",b," result : ",a+b)

sum3(3,4)# normal
sum3(b=1,a=4) #keyword
sum3(3,b=3)

def sum3(a,*b):
	add = a 
	print()
	for i in b:
		add += i
		print(i)
	print("Total is ",add)
sum3(1,2,3,4,5,6,7,8,9)














