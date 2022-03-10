
n = 10

print("\n	")
for i in range(n):
	for j in range(i):
		print(" *",end="")
	print("")

for i in range(n):
	for k in range(n,i,-1): # space
		print(" ",end="")
	for j in range(i): # character...
		print("☺ ",end="")
	print()

print("\n")


	 
