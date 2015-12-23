# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Pranav S Bijapur
# Question statement:
# Make a basic file backup program. Every 10 seconds, it should check a specified text file for any changes.
# If the file has been changed, it writes every changed line to another specified text file along with a timestamp.
# (Bonus points if you can make this work for a file in a different directory)


import time
import os

check_file = raw_input('Enter the path of file to backup: ')
backup_file = check_file.split('.')[0] + 'backup.txt'
try:
    time_interval = float(raw_input('Enter time interval in seconds: '))
except:
    # default value of time_interval is 10 seconds
    time_interval = 10
if not os.path.exists(backup_file):
    backup_file_obj = open(backup_file, 'w')
    backup_file_obj.close()  # creating a .txt file to use as backup
check_file_obj = open(check_file, 'r')
last_backup = check_file_obj.readlines()
check_file_obj.close()
while True:
    time.sleep(time_interval)  # assuming time to check and write to backup file is negligible
    backup_file_obj = open(backup_file, 'a')
    with open(check_file, 'r') as check_file_obj:
        file_list = check_file_obj.readlines()
        for line_index in range(len(file_list)):
            try:
                if file_list[line_index] != last_backup[line_index]:
                    backup_file_obj.write(time.asctime() + '     ' + file_list[line_index] + '\r\n')
            except IndexError:
                if line_index > len(last_backup) - 1:
                    backup_file_obj.write(time.asctime() + '     ' + file_list[line_index] + '\r\n')
        for line in last_backup:
            if line not in file_list:
                backup_file_obj.write(time.asctime() + '     removed ' + line + '\r\n')
        backup_file_obj.close()
        last_backup = file_list  # overwriting last_backup
