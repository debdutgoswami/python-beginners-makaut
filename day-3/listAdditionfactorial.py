import math
l = [int(i) for i in input("enter the list of elements: ").split()] #using list comprehension
s = sum(l)
avg = s/len(l)
f = [math.factorial(i) for i in l]
print("The sum is",s)
print("The average is",avg)
[print("The factorial of {} is {}".format(i,j)) for i, j in zip(l,f)]