# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 4 - PYA - 17-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Make your own module which contains some function and import it into your program.
#	module_name.func_name syntax should work as expected.
#	You can either write two different programs, or copy a function from a  previous program
#	into the imported module.

# This is where we are importing the module.

import class4soln1

print("We have just imported class4soln1. The version is {}".format(class4soln1.version))

ignore_punc_bool = True if raw_input("Ignore punctuation? y/n: ") == 'y' else False
ignore_caps_bool = True if raw_input("Ignore caps? y/n: ") == 'y' else False
string_arg = raw_input("Enter string. ")
new_string = ''.join(class4soln1.strip_punc(string_arg, ignore_punc_bool, ignore_caps_bool))
print(new_string)

# Wait a minunte, this wasn't saved in sys.path, how did it work?
# Notice the .pyc file in the same directory?
