# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:14:07 2019
@author: debdut

Program to find gcd of two number
"""
import math
a,b = (int(i) for i in input("enter two numbers: ").split())
print("the gcd is",math.gcd(a,b))