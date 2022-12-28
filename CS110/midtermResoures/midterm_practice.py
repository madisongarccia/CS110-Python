import turtle
screen = turtle.Screen()
ted=turtle.Turtle()
sideLeng=2
def draw_spiral(turtle):
	for side in range(0,100):
		ted.forward(sideLeng)
		ted.left(72)
		sideLeng=sideLeng+2
draw_spiral(ted.turtle())
