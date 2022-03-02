

# class : variable + method
'''
class = var(properties) + method(actions: process)
'''
# object

# s1 -> s -> self
class Student():

	def __init__(s1,name,marks): #constructor
		s1.name = name;
		s1.marks = marks

	def display(self):
		print(self.name,"\t",self.marks)

s = Student("PyCoder",42.54) # call constructor : s <- s1
s.display() # self <- s