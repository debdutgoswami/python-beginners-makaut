# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:35:14 2019
@author: debdut

armstrong number
"""
import math
n = int(input("enter: "))
copy=n
p = len(str(n))
s=0
while copy!=0:
    s += int(math.pow(copy%10,p))
    copy = copy//10
    
if s==n:
    print("ARMSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")