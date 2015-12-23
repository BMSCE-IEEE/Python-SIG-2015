# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 2 - PYA - 29-9-15
# Question by Pranav S Bijapur
# Solution by Pranav S Bijapur
# Question statement:
# Write a program that takes input  of the form
#	'num1,num2,[any one of +-*/]' as a string
#	and performs the given operation. In other words, your program is a simple calculator which can perform floating point arithmetic.
#	Try making improvements like asking for no.
#	of decimal digits to be displayed.

num1, num2, operation = raw_input("Enter num1,num2,operation: ").split(',')
num1 = float(num1); num2 = float(num2)
if operation == '+':
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operation == '-':
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operation == '*':
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operation == '/':
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Error.")
