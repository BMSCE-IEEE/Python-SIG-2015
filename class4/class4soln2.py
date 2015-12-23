# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 4 - PYA - 17-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
#	Make a telephone directory which maps a last name and a first name to a phone number.
#	Finally, try to sort the names alphabetically and display them to the user.


temp_first_name = None
temp_last_name = None
temp_phone_number = None
name_to_num = {}
exit_bool = False
while not exit_bool:
	try:
		temp_first_name = raw_input("Enter first name: ")
		temp_last_name = raw_input("Enter last name: ")
		temp_phone_number = int(raw_input("Enter phone number: "))
		name_to_num[(temp_last_name, temp_first_name)] = temp_phone_number
	except TypeError, e:
		print("A TypeError happened.")
		print "The error was", e
	except ValueError, e:
		print("A ValueError happened.")
		print "The error was", e
	else:
		print("Data saved successfully.")
	finally:
		print("This is getting printed no matter what.")
	print("Type 'y' to stop. ")
	exit_bool = True if raw_input() == 'y' else False
print(name_to_num)
sorted_names = []; sorted_numbers = []
for i in sorted(name_to_num.keys()):
	sorted_names.append(i)
	sorted_numbers.append(name_to_num[i])
print(sorted_names)
print(sorted_numbers)
