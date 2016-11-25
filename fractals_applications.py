'Program to generate few patterns fractals of order n, derived from pure fractals'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Nov 25, 2016'

#Add fractalsbase.py, penbase.py, and this file in the same folder
from fractalsbase import *

####Function 1
#Snowflake pattern
#Input: n = order of the snowflake. More the value of n, smaller will be deeper edges of the snowflake.
#Input: d = starting length of edge of the snowflake. Every deeper edge has a length bifurcated with nth order.
#Output: Snowflake pattern drawn with length of each edge one fourth of the input length
def snowflake(n, d):
    try:
        initiatePen()
        resetPen()
        setPenRight()
        for sides in range(3):
            koch(n, d/2, 'up', 1)
            rotate(2, 120) 
    except:
        return('Invalid input arguments')

#Example
#snowflake(2, 100)
#snowflake(3, 400)
    

####Function 2
#Cesaro in a box pattern
#Input: n = order of the cesaro. More the value of n, smaller will be deeper edges of the cesaro.
#Input: d = starting length of edge of the cesaro. Every deeper edge has a length bifurcated with nth order.
#Output: cesaro fractal formed into box.
def squaredCesaro(n, d):
    try:
        initiatePen()
        resetPen()
        setPenRight()
        for sides in range(4):
            cesaro(n, d/2 - 0.1736*d, 'down', 1)
            rotate(2, 90) 
    except:
        return('Invalid input arguments')

#Example
#squaredCesaro(2, 100)
#squaredCesaro(3, 400)
    

####Function 3
#Cesaro in a box pattern with non growing box in every order
#Input: n = order of the cesaro. More the value of n, smaller will be deeper edges of the cesaro.
#Input: d = starting length of edge of the cesaro. Every deeper edge has a length bifurcated with nth order.
#Output: cesaro fractal formed into box where the size of the box does not change when the order n is changed
def squaredCesaroNonExpanding(n, d):
    try:
        initiatePen()
        resetPen()
        setPenRight()
        for sides in range(4):
            cesaro(n, d/2 - 0.1736*d, 'down', 1)
            rotate(2, 90) 
    except:
        return('Invalid input arguments')

#Example
#squaredCesaroNonExpanding(2, 100)
#squaredCesaroNonExpanding(3, 400)
#squaredCesaroNonExpanding(4, 400)
