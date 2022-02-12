
# s = "Hello {2}, i am {0}, for my money after {1} days"

# print(s.format("Raju","shyam",25))
import random as r
import names

s = "|{:^10} | {:6} | {}"

print(s.format("Name","mark","status"))

s = "+{:^10} + {:6} + {}"
print(s.format("--------","------","------------"))

s = "|{:^10} | {:6} | {}"
for i in range(0,10):
	mark= int(r.random()*10000)
	mark = mark/100
	student = names.get_first_name()
	result = "Code"
	if mark>=33:
		result ="pass"
	else:
		result = "better luck next time"
	print(s.format(student,mark,result))
