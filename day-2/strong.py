# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:35:14 2019
@author: debdut

Strong number
"""
import math
n = int(input("enter: "))
digits = [math.factorial(int(i)) for i in str(n)]
if sum(digits)==n:
    print("STRONG NUMBER")
else:
    print("NOT STRONG NUMBER")