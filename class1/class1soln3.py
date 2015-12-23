# Python SIG 2015, BMSCE, Bangalore
# Class 1 - PYA - 12/9/2015
# Question by Tarun Verma
# Solution by Pranav S Bijapur
# Question statement:
# WAP to find average of 5 numbers

total = 0.0
for i in range(5):
    num = float(raw_input("Enter {} number: ".format(i+1)))
    total += num
average = total / 5
print "Average is", average
