import math
import statistics as stat
from datetime import datetime


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_mean = stat.mean(self.marks)
        if marks_mean > 50:
            return True
        return False


student_1 = Student("Jan Nowak", [50, 60, 70, 80, 90])
print(student_1.is_passed())

student_2 = Student("Andrzej Kowalski", [15, 20, 30, 45, 55])
print(student_2.is_passed())
