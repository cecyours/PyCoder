
 #module
def display():
	print("Hello world #60 ")

def sum(a,b=0):
	print(a,"+",b,"=",a+b)

def fun(x,y):
	display()
	sum(x,y)

def table(n):
	for i in range(1,11):
		print("{:2} x {:2} = {:2}".format(n,i,n*i))