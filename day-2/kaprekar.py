# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:35:14 2019
@author: debdut

kaprekar number
"""
import math
n = int(input("enter: "))
copy=n*n
flag = False
a1,b1 = copy//(math.pow(10,len(str(copy))//2)),copy%(math.pow(10,len(str(copy))//2))
if (a1+b1 == n and a1 and b1):
    flag = True
if len(str(copy))%2==1:
    a2,b2 = copy//(math.pow(10,(len(str(copy))//2)+1)),copy%(math.pow(10,(len(str(copy))//2)+1))
    if (a1+b1 == n and a1 and b1) or (a2+b2 == n and a2 and b2):
        flag = True
if flag:
    print("Kaprekar NUMBER")
else:
    print("NOT Kaprekar NUMBER")