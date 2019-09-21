# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:50:29 2019
@author: debdut

Program to display the bigest number among three inputted numbers using conditional operator
"""
a,b,c = (int(i) for i in input("enter the numbers: ").split())
a = a ^ ((a ^ b) & -(a < b))
a = a ^ ((a ^ c) & -(a < c))
print("greatest number is",a)