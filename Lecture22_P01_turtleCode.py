

import turtle

win = turtle.Screen()

win.bgcolor("#393939")

pen = turtle.Turtle()
pen.color("#FFFFFF")
pen.shape("turtle")
# pen.forward(130)
# pen.backward(30)

# pen.left(90)
# pen.forward(130)
# pen.backward(30)

# pen.left(90)
# pen.forward(130)
# pen.backward(30)

# pen.left(90)
# pen.forward(130)

for i in range(4):
	pen.forward(130)
	pen.backward(30)
	pen.left(90)

turtle.done()