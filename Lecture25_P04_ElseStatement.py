a = int(input("Enter a number : "))
b = int(input("Enter b number : "))

try:
	c = a/b# error 1
except:
	print("There is an error...") # if error
else:
	print("Mission passed respect +99") # if not error
finally:
	print("\nI'm a devil of my word.. ♥") # error or not error..
print("----------------")
