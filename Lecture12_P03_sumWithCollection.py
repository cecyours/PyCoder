

def code(data):
	s = 0
	for i in data:
		s+=i
	# 	print(i,end=", ")
	# print("\ntotal : ",s)
	return s

marks = [23,43,54,4,42]
avg = code(marks)/len(marks)
print("avg : ",avg,"%")