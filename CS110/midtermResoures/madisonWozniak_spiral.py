# Madison Wozniak
# Section A
# Problem 1: Spiral Square

import turtle 


def draw_spiral(turtle): 
	sideLength=2
	numSides=100
	for side in range(numSides):
		turtle.forward(sideLength)
		turtle.right(90)
		sideLength=sideLength+2

def main(): 
	screen = turtle.Screen() 
	t = turtle.Turtle()
	draw_spiral(t)
	screen.exitonclick()

main() 