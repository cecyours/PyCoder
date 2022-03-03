

import random as r
import turtle


win = turtle.Screen();
# win.bgcolor("#433033")
pen = turtle.Turtle()
turtle.write("PyCoder",font=("cooper",89,"bold"))
for i in range(100):
	pen.left(r.choice([1,4,4,4,4,4,4,4,4,4,4,90,45,120,150,53]))
	pen.forward(r.randint(100,200))
	pen.color(r.choice(["red","blue","#676232","#432244","#132244"]))
	if(i%4==0):
		pen.goto(i,0)

turtle.done();