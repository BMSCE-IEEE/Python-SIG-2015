# Python SIG in-class assignment - Class 3 - PYA - 3-10-15
# Question and Solution by Pranav S Bijapur
# Question statement:
# 	Make a dice rolling program
#	Find a module that helps you with pseudorandom generation of numbers and
#	use it to create a program to emulate a dice.
#	Then it should roll the dice until the user gets the same number three times in a row or m tries, whichever is earlier.
#	(where m is a number entered by the user at the beginning.)
#	In case of the former, it prints, 'You're lucky.'
#	Otherwise it prints 'm chances up.'

# this program has at least one bug!

import random

last_three_rolls = []
total_rolls = 0
max_chances = int(float(raw_input("Enter maximum number of chances: "))) # why int(float())?
for i in range(max_chances):
	inputval = raw_input("Roll? Reply y/n. ")
	#  this is a ternary operator in Python
	roll_bool = True if inputval == 'y' else False
	while not roll_bool:
		inputval = raw_input("Roll? Reply y to roll. n to exit. ")
		roll_bool = True if inputval == 'y' else False
		if inputval == 'n':
			exit()
	if len(last_three_rolls) < 3:
		last_three_rolls.append(roll_dice())
	else:
		last_three_rolls.pop(0)
		last_three_rolls.append(roll_dice())
		if all( j == last_three_rolls[0] for j in last_three_rolls[1:] ):	# list comprehension; try help('all'); why [1:]?
			print("You are lucky! You got three {}".format(last_three_rolls[0]))
			print(last_three_rolls)
			exit()
	total_rolls += 1
	print("Chances remaining: {}".format(max_chances - total_rolls), last_three_rolls)
print("{} chances up.".format(max_chances))


# this program won't find the function roll_dice, why?
# the error is NameError: 'roll_dice' is not defined.
# try putting a function with the same name on top, does it show an error?
def roll_dice():
	"""Returns a number from 1 to 6 (inclusive).
	Based on the random.choice method.
	"""
	return random.choice([1,2,3,4,5,6])
