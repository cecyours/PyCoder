
# single, multilevel
# A -> B : inheritance

class A(): #super, parent
	def display(self):
		print("Hello World i'm A....")

class B(A):# base, child
	def display(self):
		super().display();
		print("Hello World i'm B...")

class C(B):
	pass

x = C()
x.display()
