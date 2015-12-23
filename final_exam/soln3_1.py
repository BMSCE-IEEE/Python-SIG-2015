# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question statement:
# Import your 'value' function into another program and write a program that:
#	- prompts the user for a string
#	- calls the value function by importing the .py file where value is defined
#	- prints True if the returned "value" is even, False otherwise

# actually the question required the modification of soln1.py after
# writing it for question 1. But that file is left as it was and
# code from soln1.py is copied here for clarity.

# -- code from soln1.py --
import string


def get_string_val(check_string):
    """Returns value of stringval as specified.
    """
    stringval = 0
    check_string = check_string.lower()
    for char in check_string:
        if char in string.lowercase:
            stringval += ord(char) - ord('a')
        else:
            stringval -= 1
    return stringval
# -- end of code --
