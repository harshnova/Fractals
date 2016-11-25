Fractal patterns of nth order can be created using recursion. The base case is 0th order fractal which we need to define how it looks. 
The first order fractal will have 0th order fractal repeated on all elements of 0th order fractal itself, recursively, and every higher
order fractal will be generated as repeat of (n-1)th order fractal over all elements of (n-1)th order fractal itself.

There are three fractals demonstrated here and their applications too. The fractals are drawn on python turtle canvas, starting from 
left of the screen. So, the turtle window that pops up after function call, has to be maximized.

(1)fractalsbase.py is the base file for three fractals:
(A)Koch pattern
(B)Cesaro pattern
(C)Seirpinski triange patterns

(2)fractals_applications.py is the applications file. It shows how to draw:
(A)Snowflakes
(B)Cesaro pattern in square
(C)Cesaro pattern in non growing square

(3)penbase.py file has simplified turtle graphics functions for use in above two files.

All working examples are given in the codes.
