# Python SIG in-class assignment - Class 3 - PYA - 3-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Write a function which takes an input 'n'.
#	Then it asks for 'n' numbers and makes a list of Boolean values that are returned by a function is_greater(arg1, arg2)
#   by comparing input values in order. That is, when 4 values a, b, c and d are given. The value of the list is:
#	[a > b, b > c, c > d]. The program runs until the user types 'end'.

def is_greater(num1, num2):
	"""Checks that both arguments are numbers and of the same type.
    Returns Boolean.
"""
	assert type(num1) == type(num2), "Two different types were given."
	assert type(num1) != type(1.0) or type(num1) != type(1), "Non-number was g\
	iven."  # PEP-8 recommends 80 characters column length, shall follow it to D
	# EATH!
	return num1 > num2

bools_list = []
prev_val = raw_input("Enter a number or type 'end'. ")
userin = None
while userin != 'end':  # why not while True ?
	userin = raw_input("Enter a number or type 'end'. ")
	if userin == 'end':
		print(bools_list)
		exit()
	bools_list.append(is_greater(prev_val, userin))
	prev_val = userin
