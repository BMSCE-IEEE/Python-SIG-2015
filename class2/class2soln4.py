# Python SIG 2015, BMSCE, Bangalore
# Python SIG in-class assignment - Class 2 - PYA - 29-9-15
# Question by Tarun Verma
# Solution by Pranav S Bijapur
# Question statement:
#	Input two strings. One  takes in login_ID and other password.
#	It prints 'login_ID is successful' if password is 'password'.
#   Else should show a fail message and keep prompting user for password.


username = raw_input("Enter username: ")
password = None
while password != 'password':
    password = raw_input("Enter password: ")
    if password == 'password':
        print("Successfully logged in!")
        break  # is this break useful?
