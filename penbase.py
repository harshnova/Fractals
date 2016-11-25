'Program to simplify the use of python turtle graphics'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Nov 25, 2016'

import turtle

####Function 1
#Initiate the canvas and pen. Set canvas to black and pen to green. Make canvas and pen useable in all functions
#Input: nothing
#Output: Turtle window initiated and pointer hidden 
def initiatePen():
    try:
        global pen, canvas
        canvas = turtle.Screen()
        pen = turtle.Turtle()
        canvas.bgcolor('black')
        pen.color('green')
        pen.ht()
    except:
        return('Some error occured in initiating the pen')

#Example
#initiatePen()


####Function 2
#Clear the canvas and reset the pen to the state defined in initiatePen()
#Input: nothing
#Output: Turtle window reset with pointer at centre and hidden
def resetPen():
    try:
        canvas.clear()
        pen.reset()
        pen.ht()
        canvas.bgcolor('black')
        pen.color('green')
    except:
        return('Some error occured in resetting the pen')

#Example
#resetPen()


####Function 3
#Set the pen pointer to left of the screen to provide some room for drawing
#Input: nothing
#Output: pen pointer set to left of the screen
def setPenRight():
    try:
        pen.penup()   
        pen.left(180)
        pen.forward(550)
        pen.right(180)
        pen.pendown()
    except:
        return('Some error occured in moving pen to right of the screen')

#Example
#setPenRight()


####Function 4
#Change the color of the pen
#Input: color = pen color
#Output: pen color changed to color provided in argument
def setPenColor(color):
    try:
        pen.color(color)
    except:
        return('Invalid pen color')

#Examples
#setPenColor('green')
#setPenColor('blue')
    

####Function 5
#Draw a line
#Input: length = length of line to be drawn
#Output: a line of given length
def line(length):
    try:
        pen.forward(length)
    except:
        return('Invalid length input')

#Examples
#line(50)
#line(200)

####Function 6
#Rotate the pointer in a given direction by given degrees
#Input: direction = 1 for left turn, 2 for right turn
#Input: angle = amount of turn in degrees
#Output: the pointer rotated in the given direction by given angle
def rotate(direction, angle):
    try:
        if(direction == 1):
            pen.left(angle)
        elif(direction == 2):
            pen.right(angle)
        else:
            return('This direction is not defined')
    except:
        return('Some error occured in rotating the pen')

#Examples
#rotate(1, 60)
#rotate(2, 90)
#rotate(1, -45)


####Function 7
#Switches on or off the display of trace due to movement of pen
#Input: action = 'on' for displaying trace, 'off' of not displaying trace
#Output: trace drawing switched on or off
def trace(action):
    try:
        if(action == 'on'):
            pen.pendown()
        elif(action == 'off'):
            pen.penup()
        else:
            return('This action is not defined')
    except:
        return('Some error occured in setting the pen trace')
    
#Examples
#trace('on')
#line(100) //A line of length 50 drwan and line is visible. Pen pointer position changed to end point of the line
#trace('off')
#line(100) //A line of length 50 drwan and line is not visible. Pen pointer position changed to end point of the line
