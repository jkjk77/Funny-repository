# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:54:51 2022

@author: student
"""

def funny_fun1(numbers):
    if len(numbers) == 5:
        new_numbers = []
        for number in numbers:
            new_numbers.append(number * 2)
        return new_numbers

lista = [5, 2, 11, 9, 18]
print(funny_fun1(lista))

def funny_fun2(numbers):
    new_numbers = [number * 2 for number in numbers]
    return new_numbers

print(funny_fun2(lista))
            
        