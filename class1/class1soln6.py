# Python SIG 2015, BMSCE, Bangalore
# Class 1 - PYA - 12/9/2015
# Question by Tarun Verma
# Solution by Pranav S Bijapur
# Question statement:
# WAP to input a string with odd number of alphabets and print middlemost

str1 = raw_input("Enter string: ")
if len(str1) % 2 == 0:
    print "String has even number of characters."
elif len(str1) % 2 == 1:
    print "The character in the middle is:", str1[(len(str1)-1)/2]
else:
    print "Something went wrong."
