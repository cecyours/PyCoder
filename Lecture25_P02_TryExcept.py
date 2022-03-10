

# try:
# 	# statement errors
# except:
# 	# handle error code

# /

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
array = [1,2,3,4,5] # 0-3
try:
	c = a/b# error 1
	print(a, " / ",b," = ",c)
	print("welcome ",array[a]) #error 2
except ZeroDivisionError:
	print("There is en error... ZeroDivisionError")
except IndexError:
	print("There is an error ..IndexError")

print("----------------")
