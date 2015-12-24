# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 2 - PYA - 29-9-15
# Question by Tarun Verma
# Solution by Pranav S Bijapur
# Question statement:
# Input an angle as degrees. And find a trigonometric ratio based on users choice[out of sin, cos and tan].
# Do this 'n' times, where 'n' was entered by the user initially.

import math

n = int(raw_input('Enter n: '))
for i in range(n):
    degval = float(raw_input("Enter value in degree: "))
    radval = math.radians(degval)
    trig_ratio = None
    while trig_ratio not in ['sin', 'cos', 'tan', 'sine', 'cosine', 'tangent']:
        trig_ratio = raw_input("Enter which trig ratio you want to find: ")
    if trig_ratio == 'sin' or trig_ratio == 'sine':
        print(math.sin(radval))
    elif trig_ratio == 'cos' or trig_ratio == 'cosine':
        print(math.cos(radval))
    elif trig_ratio == 'tan' or trig_ratio == 'tangent':
        print(math.tan(radval))
    else:
        print("Wait a minute, this is not possible.")
