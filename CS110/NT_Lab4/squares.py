import turtle               # import the turtle module 
import math                 # import the math module

screen = turtle.Screen()    # open a turtle screen 
screen.bgcolor("yellow")    # set screen's background color

ted = turtle.Turtle()       # create a turtle; call it ted

sideLength = 300            #set length of first square's side to 300

num_squares=int(input())
        

for square in range(num_squares):
     for i in range(4):
          ted.forward(sideLength)    
          ted.left(90)
     ted.forward(sideLength/2)
     ted.left(45)
     sideLength=sideLength/math.sqrt(2)

screen.exitonclick()        # close screen when user clicks on it
