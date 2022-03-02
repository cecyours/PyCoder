

class Student():
	def __init__(self): #constructor
		self.name = input("Enter your name : ")
		self.rollno = int(input("Enter your rollno : "))

	def display(self):
		print("name ; ",self.name,"\trollno : ",self.rollno)

jia = Student() #setData
jia.display(); # getData