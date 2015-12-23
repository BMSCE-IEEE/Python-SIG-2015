# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question Statement:
# Write a program that reads integers until the user types 'end'.
# If any integer was entered more than once, it prints them along with the number of times they were entered.
# It also prints the sum and average of all entered numbers.


def sum_and_avg(num_list, num_dict):
    """Finds and prints sum and average of entered numbers.
    """
    print('Sum is {} and average is {}'.format(sum(num_list), float(sum(num_list))/len(num_list)))
    for num in num_dict:
        if num_dict[num] > 1:
            print('{} was entered {} times.'.format(num, num_dict[num]))


def main():
    """Function to error check and store user input.
    """
    num = raw_input('Enter number: ')
    num_list = []
    num_dict = {}
    try:
        num = int(num)
    except ValueError:
        print "Error converting to integer"
        pass
    else:
        num_list.append(num)
        num_dict[num] = num_dict.get(num, 0) + 1
    while num != 'end':
        num = raw_input('Enter number: ')
        if num == 'end':
            sum_and_avg(num_list, num_dict)
            break
        valid_num = False
        while not valid_num:
            try:
                num = int(num)
            except ValueError:
                num = raw_input('Enter valid number: ')
            else:
                valid_num = True
        num_list.append(num)
        num_dict[num] = num_dict.get(num, 0) + 1


if __name__ == '__main__':
    main()
