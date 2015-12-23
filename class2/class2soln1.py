# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 2 - PYA - 29-9-15
# Question by Tarun Verma, modified by Pranav S Bijapur
# Solution by Pranav S Bijapur
# Question statement:
# Write a program that reads two numbers from the user,
# (converting them to integers if they are floating point numbers)
# and then prints their sum along with the user input in this format:
#		'enter number 1:' 5.67
#		'enter number 2:' 5.67
#		'You entered 5.67 and 5.67. Adding 5 and 5, sum is 10'

fnum1 = float(raw_input('enter first number: '))
fnum2 = float(raw_input('enter second number: '))
num1 = int(fnum1)
num2 = int(fnum2)
print("You entered {} and {}. Adding {} and {}, sum is {}.".format(fnum1, fnum2, num1, num2, num1 + num2))
print("You entered %f and %f. Adding %d and %d, sum is %d." % (fnum1, fnum2, num1, num2, num1 + num2))
