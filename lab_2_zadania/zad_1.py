# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:50:20 2022

@author: student
"""

def function_1(list_1):
    if len(list_1) == 5:
        for x in list_1:
            print(x)

lista = ["Kuba", "Piotr", "Rafał", "Michał", "Karolina"]
lista2 = ["Kuba", "Michał"]

function_1(lista)
function_1(lista2)