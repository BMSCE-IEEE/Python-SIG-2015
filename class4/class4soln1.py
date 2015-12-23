# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 4 - PYA - 17-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Make your own module which contains some function and import it into your program.
#	module_name.func_name syntax should work as expected.
#	You can either write two different programs, or copy a function from a  previous program
#	into the imported module.

# This is the module that is being imported.

import string

version = '1.0'

# This code is taken from the palindromechecker.py of the previous class.
def strip_punc(string_arg, ignore_punc_bool, ignore_caps_bool):
	"""Removes whitespace and optionally punctuation and/or capitalization from given string.
	"""
	list_form = [i for i in string_arg] # list comprehension, how elegant!
	print list_form
	new_list_form = []
	if ignore_punc_bool:
		for i in list_form:
			if i not in string.whitespace and i not in string.punctuation:
				new_list_form.append(i)
	else:
		for i in list_form:
			if i not in string.whitespace:
				new_list_form.append(i)
	if ignore_caps_bool:
		new_list_form = [i.lower() for i in new_list_form]
	print 'new', new_list_form
	return new_list_form

def main():
	pass

if __name__ == '__main__':
	main()
# Why is this required?
