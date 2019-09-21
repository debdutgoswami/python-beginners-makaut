# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:35:14 2019
@author: debdut

perfect number
"""
n = int(input("enter: "))
digits = [int(i) for i in range(1,n) if n%i==0]
if sum(digits)==n:
    print("PERFECT NUMBER")
else:
    print("NOT PERFECT NUMBER")