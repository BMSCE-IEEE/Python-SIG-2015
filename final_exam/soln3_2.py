# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question statement:
# Import your 'value' function into another program and write a program that:
#	- prompts the user for a string
#	- calls the value function by importing the .py file where value is defined
#	- prints True if the returned "value" is even, False otherwise

import soln3_1

string1 = raw_input("Enter string: ")
if soln3_1.get_string_val(string1) % 2 == 0:
    print True
else:
    print False
