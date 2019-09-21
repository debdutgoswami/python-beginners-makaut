# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:45:56 2019
@author: debdut

Program to display the bigest number among three inputted numbers using conditional operator
"""
a,b,c = (int(i) for i in input("enter the numbers: ").split())
if b>a:
    a=b
if c>a:
    a=c
print("the greatest number is",a)