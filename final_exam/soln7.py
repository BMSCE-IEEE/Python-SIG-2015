# Python SIG 2015, BMSCE, Bangalore
# FINAL EXAM - PYA - 20/11/15
# Questions by Pranav S. Bijapur, Tarun Verma, Rahul Kumar
# Solution by Rahul Kumar
# Question statement:
# Define a class student and functions to add student (with student name as parameter) and
# delete student (with name as parameter). Name should be stored as tuple of (last name,first name)
# (where last and first names are both strings)


class Student:
    def __init__(self, name):
        self.name = tuple(name.split())[::-1]
myStudentList = []


def addStudent(name):
    myStudentList.append(Student(name))


def removeStudent(name):
    for student in myStudentList:
        if tuple(student.name) == tuple(name.split())[::-1]:
            myStudentList.remove(student)
            del(student)


def displayStudent():
    for student in myStudentList:
        for name in student.name:
            print name,
        print

while True:
    print "\n\n\n"
    print "Select an option:"
    print "1. Add a student"
    print "2. Delete student"
    print "3. Display all students"
    choice = raw_input("Enter your choice : ")
    if choice == "1":
        name = raw_input("Enter full name : ")
        addStudent(name)
    elif choice == "2":
        name = raw_input("Enter full name : ")
        removeStudent(name)
    elif choice == "3":
        displayStudent()
    else:
        print "Invalid Choice"
