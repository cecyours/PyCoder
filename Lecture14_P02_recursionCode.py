# basecase : condition to define no of repeat(calling recursion).
i = 1	
# without basecase -----------
# def display():
# 	global i 
# 	print("Hello World\t",i)
# 	i+=1
# 	display() # inner calling : recursion

# display()
# ------------ without basecase -----------


# with basecase -----------
import sys
sys.setrecursionlimit(100) #set the limit.

def display(i):
	if i==1:
		return
	print("Hello world : ",i)
	i%=2
	display(i)
	print("---------> ",i)

# display(5)

# 5! = 5x4!
# 4! = 4x3!
# 3! = 3*2!
def fact(f):
	print("data : ",f)
	if f==1: #basecase
		return f
	return f*fact(f-1)
	# print("Data : ",x)

ans = fact(5)
print("fact : ",ans)