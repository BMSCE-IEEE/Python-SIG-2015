# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question statement:
# Write a program that calculates the 'value' of a string. It should prompt the user for a string and print the "value"
#   Calculate value using the following scheme:
#	a/A - 0
#	b/B - 1
#	...
#	z/Z - 25
#	any other character - -1
# Example: 'abc:(*&(*^&^*AAAAAAA' = 1 + 2 - 10 = -7

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

check_string = raw_input('Enter string: ')
stringval = get_string_val(check_string)
print stringval
