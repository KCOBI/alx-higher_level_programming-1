#!/usr/bin/python3
"""
    10-student: class Student
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:

            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            print(type(self.__dict__.keys()), "xxxxxxxxxxxxx", type(attr))
            return res
        else:
            return self.__dict__


student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
