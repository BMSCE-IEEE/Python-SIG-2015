# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 2 - PYA - 29-9-15
# Question by Tarun Verma
# Solution by Pranav S Bijapur
# Question statement:
#	Find the factorial of a given number. Don't import math.
#	Try to make your program break and fix all those cases. (recursive vs. iterative)


def factorial(n):
    assert type(n) == type(1), "Argument to factorial function must be an integer."
    assert n >= 0, "Argument to factorial function can not be negative."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# nothing happens when we run this program, why?
