# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:35:14 2019
@author: debdut

palindrome
"""
n = input("enter: ")
if n[::-1]==n:
    print("palindrome")
else:
    print("not palindrome")