# Python SIG 2015, BMSCE, Bangalore
# Python SIG - Class 5 - PYA - 7-11-15
# Example of a sample class
# By Rahul Kumar


class StudentInfo(object):
    """My Sample Class"""
    countStudent = 0
    LastStudent = ""

    def __init__(self, name, usn, age):
        self.name = name
        self.usn = usn
        self.age = age
        StudentInfo.countStudent += 1
        StudentInfo.LastStudent = name

    def displayRecord(self):
        print "Name :", self.name
        print "USN :", self.usn
        print "Age :", self.age
