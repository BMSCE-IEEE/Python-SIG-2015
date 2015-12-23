# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question statement:
# Many list methods return None and modify the list. Define a function "modifier" that
# returns the modified form of the list instead of None
#	- function inputs are the method as a string (eg. 'append') and the list
#     and any other parameters required by the list 	method
#	- return value is the list modified by the input method
#     Example: a = [1, 2, 3]
#	    b = a.append(4)
#	    (here b = None and a = [1, 2, 3, 4] so you can't do
#	    a = a.append(4))
#	    a = [1, 2, 3]
#	    a = modifier(a, 'append', 4)
#	    (here a = [1, 2, 3, 4])
#	(Ignore double underscore methods and those that don't return None)


# listing (heh.) the methods in the order of arguments required,
# reverse, sort: 0
# append: 1, element
# extend: 1, list
# pop: 1, index
# remove: 1, element
# insert: 2, index, element

def modifier(method_name, input_list, arg1='default', arg2='default'):
    if arg1 == 'default' and arg2 == 'default':
        if method_name == 'reverse':
            input_list.reverse()
        elif method_name == 'sort':
            input_list.sort()
    elif arg1 != 'default' and arg2 == 'default':
        if method_name == 'append':
            input_list.append(arg1)
        elif method_name == 'extend':
            input_list.extend(arg1)
        elif method_name == 'pop':
            if arg1 < len(input_list):
                input_list.pop(arg1)
        elif method_name == 'remove':
            if arg1 in input_list:
                input_list.remove(arg1)
    elif arg1 != 'default' and arg2 != 'default':
        if method_name == 'insert':
            assert type(arg1) == type(1)
            input_list.insert(arg1, arg2)
    return input_list


def convert_to_num(arg):
    ''' Tries to convert arg to number, from string, if possible.
    '''
    try:
        arg = float(arg)
        # to convert to int when possible
        if arg == int(arg):
            arg = int(arg)
    except:
        pass
    return arg


def convert_to_num_wrapper(arg):
    ''' Wrapper for convert_to_num.
    '''
    if type(arg) == type(list()) or type(arg) == type(tuple()):
        return_list = []
        for element in arg:
            return_list.append(convert_to_num(element))
    else:
        return_list = convert_to_num(arg)
    return return_list


# hardcoding value of input_list for simplicity
# can be taken from user using convert_to_num function
input_list = [1, 2, 3]
method_name = raw_input('Enter method_name: ')
if method_name == 'reverse' or method_name == 'sort':
    input_list = modifier(method_name, input_list)
elif method_name == 'append':
    arg1 = raw_input('Enter value to append: ')
    arg1 = convert_to_num_wrapper(arg1)
    input_list = modifier('append', input_list, arg1)
elif method_name == 'extend':
    arg1 = raw_input('Enter list to extend: ')
    arg1 = arg1.replace(' ', '')[1:-1]
    arg1 = list(arg1.split(','))
    arg1 = convert_to_num_wrapper(arg1)
    arg1_modified = []
    for element in arg1:
        if type(element) == type(''):
            element = element[1:-1]
        arg1_modified.append(element)
    input_list = modifier('extend', input_list, arg1_modified)
elif method_name == 'pop':
    arg1 = raw_input('Enter index to pop: ')
    arg1 = convert_to_num_wrapper(arg1)
    input_list = modifier('pop', input_list, arg1)
elif method_name == 'remove':
    arg1 = raw_input('Enter element to remove: ')
    arg1 = convert_to_num_wrapper(arg1)
    input_list = modifier('remove', input_list, arg1)
elif method_name == 'insert':
    # supports only int, float and strings
    arg1 = convert_to_num_wrapper(raw_input('Enter index to insert at: '))
    arg2 = convert_to_num_wrapper(raw_input('Enter element to insert: '))
    input_list = modifier('insert', input_list, arg1, arg2)
print input_list
