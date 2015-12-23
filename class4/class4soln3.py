# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 4 - PYA - 17-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Write a program to display the number of times a particular alphabet appears in a string.
#	For example 'aabbBc' should return
#	a was present 2 times
#	b was present 2 times
#	B was present 1 time
#	c was present 1 time

from class4soln1 import strip_punc

ignore_punc_bool = True
ignore_caps_bool = False
string_arg = raw_input("Enter string. ")
new_string = ''.join(strip_punc(string_arg, ignore_punc_bool, ignore_caps_bool))
alphabet_to_num = {}
for i in new_string:
    alphabet_to_num[i] = alphabet_to_num.get(i, 0) + 1
for i in alphabet_to_num:
    if alphabet_to_num[i] == 1:
        print("{} was present 1 time.".format(i))
    else:
        print("{} was present {} times.".format(i, alphabet_to_num[i]))
