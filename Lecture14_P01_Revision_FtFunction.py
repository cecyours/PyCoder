

def table(num):
	for i in range(1,11):
		print("{:2} x {:2} = {:2}".format(num,i,num*i))
n = int(input("Enter number : "))
table(n)
print("---------------------")
# fact : 5x4x3x2x1
# [start:end:step]
def fact(n=2):
	f = 1
	for i in range(n,0,-1):
		f*=i
		print("{:2} , {:2} ".format(i,f))

fact(5)
print("---------------------")
fact()


