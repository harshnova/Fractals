'Program to generate few fractals of order n'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Nov 25, 2016'

#Add fractalsbase.py, penbase.py, and this file in the same folder
from penbase import *

####Function 1
#koch fractal
#Input: n = order of koch.
#Input: d = starting length of edge of the koch for 0th order. Every deeper edge has a length bifurcated with nth order.
#Input: v = vertical direction of koch.
#Input: i = initiation flag. shall be always 0. This is to initiate the canvas and pen just once when the function is called. We dont want recursion to reset it again.
#Output: koch pattern of order n
def koch(n, d, v, i):
    try:
        verticalDirections = ['up','down']
        if(i == 0):
            initiatePen()
            resetPen()
            setPenRight()
        if(n == 0):
            line(d)
        else:
            for angle in [60, -120, 60, 0]:
                koch(n-1, d/2, v, 1)
                rotate(verticalDirections.index(v) + 1, angle)                                    
    except:
        return('Invalid input arguments')

#Examples
#koch(0, 100, 'up', 0)
#koch(1, 200, 'down', 0)
#koch(2, 200, 'up', 0)
    

####Function 2
#cesaro fractal
#Input: n = order of cesaro.
#Input: d = starting length of edge of cesaro for 0th order. Every deeper edge has a length bifurcated with nth order.
#Input: v = vertical direction of cesaro.
#Input: i = initiation flag. shall be always 0. This is to initiate the canvas and pen just once when the function is called. We dont want recursion to reset it again.
#Output: cesaro pattern of order n
def cesaro(n, d, v, i):
    try:
        verticalDirections = ['up','down']
        if(i == 0):
            initiatePen()
            resetPen()
            setPenRight()
        if(n == 0):
            line(d)
        else:
            for angle in [85, 190, 85, 0]:
                cesaro(n-1, d/2, v, 1)
                rotate(verticalDirections.index(v) + 1, angle)                                    
    except:
        return('Invalid input arguments')

#Examples
#cesaro(0, 100, 'up', 0)
#cesaro(1, 200, 'down', 0)
#cesaro(2, 200, 'up', 0)


####Function 2
#sierpinski triangles
#Input: n = order of sierpinski.
#Input: d = starting length of edge of sierpinski equilateral triangle for 0th order. Every deeper edge has a length bifurcated with nth order.
#Input: i = initiation flag. shall be always 0. This is to initiate the canvas and pen just once when the function is called. We dont want recursion to reset it again.
#Output: sierpinski triangles of order n
def sierpinski(n, d, i):
    try:
        if(i == 0):
            initiatePen()
            resetPen()
            setPenRight()
        if(n == 0):
            for j in range(3):
                line(d)
                rotate(1, 120)
        else:
            sierpinski(n-1, d/2, 1)
            trace('off')
            line(d/2)
            trace('on')
            sierpinski(n-1, d/2, 1)
            rotate(1, 120)
            trace('off')
            line(d/2)
            trace('on')
            rotate(2, 120)
            sierpinski(n-1, d/2, 1)
            rotate(2, 120)
            trace('off')
            line(d/2)
            trace('on')
            rotate(1,120)
    except:
        return('Invalid input arguments')
    
#Examples
#sierpinski(0, 100, 0)
#sierpinski(1, 200, 0)
#sierpinski(2, 500, 0)
