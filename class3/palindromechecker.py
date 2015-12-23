# Python SIG in-class assignment - Class 3 - PYA - 3-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Palindrome checker
#	Write a palindrome checker.
#	That's it. Up to you how complex you make it.


import string

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

pal_string = raw_input("Enter string. ")
confirmed_bool = False; is_pal_bool = None
while not confirmed_bool:
	print # what does this do?
	print r"{}".format(pal_string) # raw strings
	tempval = raw_input("This is the string. 'y' to confirm. ")
	confirmed_bool = True if tempval == 'y' else False
	if not confirmed_bool:
		pal_string = raw_input("Re-type string: ")
ignore_punc_bool = True if raw_input("To ignore punctuation enter 'y'. ") == 'y' else False
ignore_caps_bool = True if raw_input("To ignore capitalization enter 'y'. ") == 'y' else False
print 'p', ignore_punc_bool, 'c', ignore_caps_bool
first_form = strip_punc(pal_string, ignore_punc_bool, ignore_caps_bool)
second_form = first_form[::-1]
is_pal_bool = first_form == second_form
if ignore_caps_bool and ignore_punc_bool:
	print("Ignoring capitalization and punctuation,")
elif ignore_caps_bool:
	print("Ignoring capitalization not punctuation,")
elif ignore_punc_bool:
	print("Ignoring punctuation not capitalization,")
print("We are comparing:")
print first_form
print "with"
print second_form
print
if is_pal_bool:
	print("Given string is a palindrome.")
else:
	print("Given string is not a palindrome")
