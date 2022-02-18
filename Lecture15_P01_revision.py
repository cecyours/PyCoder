

# recursion : function calls itself
# def display():
# 	print("Hello World")
# 	display();

# display();
# 10
import sys
sys.setrecursionlimit(10)
x = sys.getrecursionlimit() # 10
print("Code : ",x)

i=1
def code():
	global i
	print(i)
	if(i==5):
		return
	i+=1
	code()

code();
