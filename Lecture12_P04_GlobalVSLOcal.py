
salary = 2000

def increment():
	global salary
	salary = 3000
	print("2 : ",salary)

print("1 : ",salary) # 2000
increment() # call
print("3 : ",salary) # ??