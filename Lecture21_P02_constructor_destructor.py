


class A():
	'''
		This is my code
	'''
	def __init__(self,name="Home"): #constructor
		print("Phase 1",self)

	def display(self):
		print("I'm here ♥")

	def __del__(self): #destructor
		print("I'm out ☻",self)

s1 = A()
s2 = A()
print(s1.__doc__)

s1.display()
# del s2 
# del s1 #delete s
# # s.display();
input("waiting to exit....")
print(print.__doc__)

import random
print(random.__doc__)




