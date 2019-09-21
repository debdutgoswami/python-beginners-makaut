# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:17:08 2019
@author: debdut
"""
n = 5 #considering no of rows to be 5

"""
*
**
***
"""
print("PATTERN 1")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
    
"""
***
**
*
"""
print("PATTERN 2")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    
"""
  *
 ***
*****
"""
print("PATTERN 3")
for i in range(n):
    for j in range(i+1,n):
        print(end=" ")
    for j in range(2*(i+1)-1):
        print("*",end="")
    print()

"""
1
2 3
4 5 6
"""
print("PATTERN 4")
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()
    
"""
A
A B
A B C
"""
print("PATTERN 5")
for i in range(n):
    ch = 'A'
    for j in range(i+1):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
    print()