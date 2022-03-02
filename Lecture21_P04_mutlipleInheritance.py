
# A -> C
# B -> C


class A():
	def display(self):
		print("I'm A")

class B():
	def display(self):
		print("I'm B")

class C(B,A):
	pass

x = C()
x.display()