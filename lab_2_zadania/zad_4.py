# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:03:11 2022

@author: student
"""

def funny_fun(numbers):
    [print(num) for num in numbers[::2]]

funny_range = range(1, 11)

funny_fun(funny_range)